from typing import Any, Dict, Callable

def generic_parser_fallback(result: Any, *args, **kwargs) -> Dict[str, Any]:
    response_data: Dict[str, Any] = {
        "content": None,
        "usage": {
            "prompt_tokens": 0,
            "completion_tokens": 0,
            "total_tokens": 0
        },
        "model": None,
        "id": None,
        "created": None,
        "data": None
    }

    # Extract common fields
    if hasattr(result, 'model'):
        response_data['model'] = result.model
    if hasattr(result, 'prompt_feedback'):
        response_data['prompt_feedback'] = result.prompt_feedback

    # Handle content
    if hasattr(result, 'text'):
        response_data['content'] = result.text
    elif hasattr(result, 'candidates') and result.candidates:
        response_data['content'] = result.candidates[0].content.parts[0].text

    # Handle usage (Note: Gemini might not provide token usage in the same way)
    if hasattr(result, 'usage'):
        response_data['usage'] = {
            "prompt_tokens": getattr(result.usage, 'prompt_token_count', 0),
            "completion_tokens": getattr(result.usage, 'candidate_token_count', 0),
            "total_tokens": getattr(result.usage, 'total_token_count', 0)
        }

    # Handle finish reason
    if hasattr(result, 'finish_reason'):
        response_data['finish_reason'] = result.finish_reason

    # Handle errors generically
    if isinstance(result, Exception):
        response_data['error'] = {
            'message': str(result),
            'type': type(result).__name__,
            'param': None,
            'code': None
        }

    return response_data


gemini_custom_methods: Dict[str, Callable] = {
    "generic_parser_fallback": generic_parser_fallback,
}
