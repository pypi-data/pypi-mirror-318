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
        "data": None  # Initialize 'data' as None
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

    # Handle 'choices' which is present in completions and chat completions
    if hasattr(result, 'choices') and result.choices:
        choice = result.choices[0]
        if hasattr(choice, 'text'):  # For completions
            response_data['content'] = choice.text
        elif hasattr(choice, 'message'):  # For chat completions
            response_data['content'] = choice.message.content
            response_data['role'] = choice.message.role
            if hasattr(choice.message, 'function_call'):
                response_data['function_call'] = choice.message.function_call
        if hasattr(choice, 'finish_reason'):
            response_data['finish_reason'] = choice.finish_reason

    # Handle embeddings
    if hasattr(result, 'data') and isinstance(result.data, list):
        response_data['data'] = [
            {'embedding': item.embedding, 'index': item.index}
            for item in result.data
        ]

    # Handle audio transcriptions/translations
    if hasattr(result, 'text'):
        response_data['content'] = result.text

    # Handle errors
    if hasattr(result, 'error'):
        response_data['error'] = {
            'message': result.error.message,
            'type': result.error.type,
            'param': getattr(result.error, 'param', None),
            'code': getattr(result.error, 'code', None)
        }

    return response_data


openai_custom_methods: Dict[str, Callable] = {
    "generic_parser_fallback": generic_parser_fallback,
}
