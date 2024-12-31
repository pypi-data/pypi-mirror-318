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
    common_fields = ['id', 'model', 'created', 'usage']
    for field in common_fields:
        if hasattr(result, field):
            if field == 'usage':
                response_data['usage'] = {
                    "prompt_tokens": getattr(result.usage, 'prompt_tokens', 0),
                    "completion_tokens": getattr(result.usage, 'completion_tokens', 0),
                    "total_tokens": getattr(result.usage, 'total_tokens', 0)
                }
            else:
                response_data[field] = getattr(result, field)

    # Handle 'completion' which is present in Anthropic's response
    if hasattr(result, 'completion'):
        response_data['content'] = result.completion

    # Handle 'stop_reason' which is similar to OpenAI's 'finish_reason'
    if hasattr(result, 'stop_reason'):
        response_data['finish_reason'] = result.stop_reason

    # Handle errors generically
    if isinstance(result, Exception):
        response_data['error'] = {
            'message': str(result),
            'type': type(result).__name__,
            'param': None,
            'code': None
        }

    return response_data


anthropic_custom_methods: Dict[str, Callable] = {
    "generic_parser_fallback": generic_parser_fallback,
}
