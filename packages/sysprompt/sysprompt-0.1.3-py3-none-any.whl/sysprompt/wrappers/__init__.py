from .openai import openai_custom_methods
from .anthropic import anthropic_custom_methods
from .gemini import gemini_custom_methods


WRAPPERS = {
    "openai": openai_custom_methods,
    "anthropic": anthropic_custom_methods,
    "gemini": gemini_custom_methods,
}
