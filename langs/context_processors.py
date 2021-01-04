from .services import get_all_languages


def languages_processor(request):
    """Add all languages in each context"""
    all_languages = get_all_languages()
    return {'languages': all_languages}
