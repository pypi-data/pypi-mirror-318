import json
import os
import logging
import functools
import requests
import time
import types
import contextlib
import threading
from collections import deque
from typing import Dict, List, TypeVar, Generic, Any, cast, Callable, Optional
from decimal import Decimal
from .cache import PromptCache


T = TypeVar('T')


class SysPrompt:
    """
    A client for the SysPrompt API.
    """

    BASE_URL: str = "https://api.sysprompt.com"
    PROMPT_RETRIEVAL_PATH: str = "sdk/prompts/{code_id}/"
    PROMPT_LOGGING_PATH: str = "sdk/logs/prompt/"
    API_VERSION: str = "v1"

    def __init__(self, api_key: Optional[str], raise_on_error: bool = False, default_cache_ttl: int = 900):
        """
        Initialize the SysPrompt client.
        api_key: Your project API key.
        raise_on_error: Whether to raise an exception on API errors. In development, you may want to set this to True
            so that you can see what's going wrong. In production, you can set it to False so that SysPrompt
            silently ignores errors of its own making. No worries that the LLM client API will raise errors as usual.
        default_cache_ttl: The default TTL for prompts in seconds. Use 0 to disable caching.
        """
        project_api_key: Optional[str] = api_key or os.environ.get("SYSPROMPT_PROJECT_API_KEY", "")
        if not project_api_key:
            raise SysPromptException(
                "Project API key must be provided or set in SYSPROMPT_PROJECT_API_KEY environment variable"
            )
        self.api_key: str = project_api_key
        self._wrappers: Dict[str, Dict[str, Callable]] = {}
        self._prompts_cache: PromptCache = PromptCache(default_ttl=default_cache_ttl)
        self._captured_times: Dict[int, float] = {}
        self._raise_on_error: bool = raise_on_error
        self._thread_local = threading.local()
        self._rate_limiter: RateLimiter = RateLimiter(max_calls=256, period=60)

    def preload_prompts(self, code_ids: Optional[List[str]] = None):
        """
        Preload prompts into the cache.
        If you are using the SysPrompt Prompts CMS, you can preload the prompts
        that your program needs.

        Best practice is to call this method at the beginning of your program,
        and then use the `wrap` method to wrap your LLM client.

        Prefetching prompts is optional, but it can improve performance if you
        know which prompts your program uses.

        If you don't specify the code_ids, then it will prefetch 100 prompts
        from your project based on creation date (oldest first). New prompts
        will be fetched on demand and will be cached for subsequent use during
        the same request/program execution.

        Args:
        code_ids (Optional[List[str]]): List of prompt code IDs to preload.
        If None, fetches the 100 oldest prompts from the project.
        """
        prompts: List[dict] = []
        if code_ids is None:
            prompts = list(self._api_request('GET', 'sdk/prompts/'))
        else:
            prompts = list(self._api_request('POST', 'sdk/prompts/', {'code_ids': code_ids}))

        for prompt in prompts:
            self._prompts_cache.set(prompt['code_id'], None, prompt)

    def get_prompt(self, code_id: str, version: Optional[str] = None) -> str | dict | list:
        """
        Retrieve a prompt from the SysPrompt API.

        Args:
            code_id (str): The unique identifier for the prompt.
            version (Optional[str]): The version of the prompt to retrieve, empty for the default version.
        Returns:
            str | dict | list: The prompt data.

        Raises:
            SysPromptException: If the API request fails.
        """
        cached_prompt = self._prompts_cache.get(code_id, version)
        if cached_prompt is not None:
            return cached_prompt.get('content', [])

        try:
            if not code_id:
                raise SysPromptException("Prompt code ID is required. Got empty string.")
            version_string = f"?version={version}" if version else ""
            prompt = self._api_request('GET', f"{self.PROMPT_RETRIEVAL_PATH.format(code_id=code_id)}{version_string}")
            if prompt:
                self._prompts_cache.set(code_id, version, prompt)
            return prompt.get('content', [])
        except Exception as e:
            if self._raise_on_error:
                raise e
            else:
                logging.warning(str(e))
        return ''

    def compile(
        self,
        prompt_id: str | None = None,
        params: dict = {},
        version: Optional[str] = None,
        prompt_object: None | str | dict | list = None,
    ) -> str | dict | list:
        """
        Compile a prompt with the given parameters.
        You can either provide a prompt code ID or a prompt object.

        Args:
            prompt_id (str): The unique identifier for the prompt.
            params (dict): The parameters to substitute into the prompt.
            version (str): The version of the prompt to retrieve, empty for the default version.
            prompt_object (str | dict | list): The prompt object to compile.
        Returns:
            str | dict | list: The compiled prompt.
        """

        prompt: str | dict | list | None = self.get_prompt(prompt_id, version) if prompt_id else prompt_object
        if not prompt:
            if self._raise_on_error:
                raise SysPromptException("Prompt not found")
            else:
                logging.warning("Prompt not found")
                return ''

        def replace_placeholders(obj: str | dict | list) -> str | dict | list:
            if isinstance(obj, str):
                for param_key, param_value in params.items():
                    placeholder = f"{{{{{param_key}}}}}"
                    obj = obj.replace(placeholder, str(param_value))
                return obj
            elif isinstance(obj, dict):
                return {k: replace_placeholders(v) for k, v in obj.items()}
            elif isinstance(obj, list):
                return [replace_placeholders(item) for item in obj]
        prompt = replace_placeholders(prompt)
        if isinstance(prompt, str):
            try:
                return json.loads(prompt)
            except (json.JSONDecodeError, TypeError):
                return prompt
        return prompt

    def log(self,
            call_properties: dict,
            llm_response: Optional[dict],
            time_taken: Optional[float] = None,
            completion_tokens: Optional[int] = None,
            prompt_tokens: Optional[int] = None,
            total_tokens: Optional[int] = None,
            cached_tokens: Optional[int] = None,
            cost: Optional[Decimal] = None,
            score: Optional[float] = None,
            prompt_id: Optional[str] = None,
            trace_id: Optional[str] = None,
            llm_response_successful: bool = True,
            metadata: Optional[dict] = None) -> str:
        """
        Log the execution of a prompt.

        Args:
            data (dict): A dictionary containing the following fields:
                - call_properties (dict): Properties of the API call (optional)
                - llm_response (dict): The response from the LLM (optional)
                - time_taken (float): Time taken for the operation (optional)
                - completion_tokens (int): Number of completion tokens (optional)
                - prompt_tokens (int): Number of prompt tokens (optional)
                - total_tokens (int): Total number of tokens (optional)
                - cached_tokens (int): Number of cached tokens (optional)
                - cost (Decimal): Cost of the operation (optional)
                - score (float): Score of the operation (optional)
                - prompt_id (str): The ID of the prompt (optional)
                - trace_id (str): The ID of the associated trace (optional)
                - llm_response_successful (bool): Whether the LLM response was successful (optional)
                - metadata (dict): Additional metadata (optional)
        Returns:
            str: The UUID of the logged PromptLog entry.
        """
        """
        Log the execution of a prompt.

        Args:
            data (dict): The data to log.

        Returns:
            Dict[str, Any]: The logged data.
        """
        if not self._rate_limiter.can_make_call():
            if self._raise_on_error:
                raise SysPromptException("Rate limit exceeded. Please try again later.")
            else:
                logging.warning("Rate limit exceeded. Please try again later.")
                return ''

        self._rate_limiter.add_call()

        if time_taken is None:
            time_taken = getattr(self._thread_local, 'captured_time', None)
            if time_taken is not None:
                delattr(self._thread_local, 'captured_time')

        try:
            data: dict = {
                "call_properties": call_properties,
                "llm_response": llm_response,
                "time_taken": time_taken,
                "completion_tokens": completion_tokens,
                "prompt_tokens": prompt_tokens,
                "total_tokens": total_tokens,
                "cached_tokens": cached_tokens,
                "cost": cost,
                "score": score,
                "prompt_id": prompt_id,
                "trace_id": trace_id,
                "llm_response_successful": llm_response_successful,
                "metadata": metadata,
            }
            response_data: dict = self._api_request('POST', self.PROMPT_LOGGING_PATH, data)
            if 'uuid' in response_data:
                return response_data['uuid']
        except Exception as e:
            if self._raise_on_error:
                raise SysPromptException(f"Exception while logging prompt: {e}")
            else:
                logging.warning(f"Exception while logging prompt: {e}")
        if self._raise_on_error:
            raise SysPromptException("Prompt logging failed")
        else:
            logging.warning("Prompt logging failed")
        return ''

    async def log_async(self, *args, **kwargs):
        """
        Async logging is not implemented yet.
        """
        raise NotImplementedError("Async logging is not implemented yet.")

    def wrap(self, ai_client: T) -> T:
        """
        Wrap an LLM client to automatically log all calls to the SysPrompt API.
        """
        try:
            client_name = ai_client.__name__.lower()
        except AttributeError:
            client_name = ai_client.__class__.__name__.lower()
        if any(name in client_name for name in ['google', 'gemini', 'generative']):
            client_name = 'gemini'
        if client_name not in self._wrappers:
            self.load_wrapper(client_name)
        return cast(T, AIWrapper(self, ai_client, self._wrappers.get(client_name, {})))

    def load_wrapper(self, name: str):
        """
        Load a wrapper with the custom methods for the given LLM client.
        """
        try:
            from sdk.wrappers import WRAPPERS
            self._wrappers[name] = WRAPPERS.get(name, {})
        except ImportError:
            logging.warning(f"Warning: No wrapper found for {name}")
        except KeyError:
            logging.warning(f"Warning: No wrapper defined for {name}")

    @contextlib.contextmanager
    def capture_time(self):
        """
        This is a context manager to capture the time taken for a block of code execution
        and automatically add it to the next log call.

        Usage:
            with sysprompt.capture_time():
                openai.chat.create()...
            sysprompt.log(...)  # time_taken will be automatically added
        """
        start_time = time.time()
        try:
            yield
        finally:
            end_time = time.time()
            captured_time = end_time - start_time
            self._thread_local.captured_time = captured_time

    def _api_request(self, method: str, path: str, data: Optional[dict] = None) -> dict:
        """
        Make an API request to the SysPrompt API. It will retry the request
        if it fails due to a network error or a server error.

        Args:
            method (str): The HTTP method to use.
            path (str): The path to append to the base URL.
            data (dict): The data to send in the request body.

        Returns:
            dict: The response data.

        Raises:
            SysPromptAPIError: If the API request fails.
            SysPromptAuthError: If the project key is invalid.
        """
        max_retries = 3
        base_delay = 1  # Initial delay in seconds
        exception: Optional[Exception] = None

        for attempt in range(max_retries):
            try:
                url: str = self._get_url(path)
                print(url)
                response: requests.Response = requests.request(method, url, json=data, headers=self._get_headers())
                response.raise_for_status()
                return response.json()
            except requests.HTTPError as e:
                status_code = e.response.status_code
                if status_code == 401:
                    exception = SysPromptAuthError(
                        "Project key is invalid. Check your API key and SysPrompt account."
                    )
                    if self._raise_on_error:
                        raise exception
                    else:
                        logging.warning(str(exception))
                        return {}
                elif status_code >= 500 and attempt < max_retries - 1:
                    # Server error, retry
                    delay = base_delay * (2 ** attempt)  # Exponential backoff
                    time.sleep(delay)
                    continue
                else:
                    exception = SysPromptAPIError(
                        f"API operation failed. Got status code: {status_code}. Check your API key and parameters."
                    )
                    if self._raise_on_error:
                        raise exception
                    else:
                        logging.warning(str(exception))
                        return {}
            except requests.RequestException as e:
                if attempt < max_retries - 1:
                    # Network-related error, retry
                    delay = base_delay * (2 ** attempt)  # Exponential backoff
                    time.sleep(delay)
                    continue
                if self._raise_on_error:
                    raise e
                else:
                    logging.warning(str(e))
                    return {}
            except Exception as e:
                if self._raise_on_error:
                    raise e
                else:
                    logging.warning(str(e))
                    return {}

        # This line should only be reached if all retries failed
        return {}

    def _get_url(self, path: str) -> str:
        """
        Get the full URL for the given path.

        Args:
            path (str): The path to append to the base URL.

        Returns:
            str: The full URL.
        """
        return f"{self.BASE_URL}/{self.API_VERSION}/{path}"

    def _get_headers(self) -> dict:
        """
        Get the headers for the API request.

        Returns:
            dict: The headers.
        """
        return {"X-PROJECT-KEY": self.api_key}


class AIWrapper(Generic[T]):

    def __init__(
            self,
            sysprompt_client: 'SysPrompt',
            ai_client: T,
            custom_methods: Dict[str, Callable],
            path: List[str] = []):
        self.sysprompt: SysPrompt = sysprompt_client
        self.client: T = ai_client
        self.custom_methods: Dict[str, Callable] = custom_methods
        self.path: List[str] = path or []

    def __getattr__(self, name: str) -> Any:
        """
        Get an attribute from the wrapped LLM client.
        """
        attr: Any = getattr(self.client, name)
        new_path: List[str] = self.path + [name]
        if isinstance(attr, (types.MethodType, types.FunctionType)):
            return self._wrap_callable(attr, new_path)
        elif callable(attr):
            return self._wrap_nested(attr, new_path)
        return self._wrap_nested(attr, new_path)

    def __call__(self, *args, **kwargs) -> Any:
        """
        Call the wrapped LLM client.
        We need to wrap the call to the LLM client itself, so that we can capture
        the time taken and results for the call and add it to the log.
        """
        if callable(self.client):
            return self._wrap_callable(self.client, self.path + ['__call__'])(*args, **kwargs)
        raise TypeError(f"{self.client.__class__.__name__} object is not callable")

    def _wrap_nested(self, obj: T, path: List[str]) -> 'AIWrapper':
        """
        Wrap a nested attribute of the LLM client.
        This is used for methods that return another callable, like nested objects
        or methods with arguments.
        """
        return AIWrapper(self.sysprompt, obj, self.custom_methods, path)

    def _wrap_callable(self, func: Callable, path: List[str]) -> Callable:
        """
        Wrap a callable attribute of the LLM client.
        This is used for methods that don't return another callable, like queries
        or other methods that return a final result.
        """
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            full_path: str = '.'.join(path)
            custom_method: Optional[Callable] = self.custom_methods.get(full_path) if callable(self.custom_methods.get(full_path)) else None
            generic_parser_fallback: Optional[Callable] = self.custom_methods.get('generic_parser_fallback')
            try:
                with self.sysprompt.capture_time():
                    result: Any = func(*args, **kwargs)
                    result_for_log: Any = result
                    if custom_method:
                        result_for_log = custom_method(result, *args, **kwargs)
                    elif generic_parser_fallback:
                        result_for_log = generic_parser_fallback(result, *args, **kwargs)
                self._log_success(full_path, args, kwargs, result_for_log)
                return result

            except Exception as e:
                self._log_error(full_path, args, kwargs, e)
                raise

        return wrapper

    def _log_start(self, method_name: str, args: tuple, kwargs: dict) -> None:
        """
        Log the start of a method call.
        """
        pass

    def _log_success(self, method_name: str, args: tuple, kwargs: dict, result: Any) -> None:
        """
        Log the success of a method call.
        """
        llm_response = result.get('content') if result.get('content') else result
        del result['content']

        self.sysprompt.log(
            call_properties=kwargs,
            llm_response=llm_response,
            prompt_tokens=result.get('usage', {}).get('prompt_tokens'),
            completion_tokens=result.get('usage', {}).get('completion_tokens'),
            total_tokens=result.get('usage', {}).get('total_tokens'),
            metadata={
                "method_name": method_name,
                "path": '.'.join(self.path),
                "info": result,
            },
        )

    def _log_error(self, method_name: str, args: tuple, kwargs: dict, error: Exception) -> None:
        """
        Log the error of a method call
        """
        self.sysprompt.log(
            call_properties=kwargs,
            llm_response=dict(error=str(error)),
            metadata={"method_name": method_name},
            llm_response_successful=False,
        )


class RateLimiter:
    """
    A simple rate limiter to keep the SysPrompt API healthy.
    """
    def __init__(self, max_calls: int, period: int):
        self.max_calls: int = max_calls
        self.period: int = period
        self.calls: deque = deque()

    def add_call(self):
        now = time.time()
        self.calls.append(now)

        while self.calls and self.calls[0] <= now - self.period:
            self.calls.popleft()

    def can_make_call(self):
        return len(self.calls) < self.max_calls


class SysPromptException(Exception):
    """Base exception for SysPrompt SDK"""


class SysPromptAPIError(SysPromptException):
    """Raised when an API request fails"""


class SysPromptAuthError(SysPromptException):
    """Raised when there's an authentication error"""
