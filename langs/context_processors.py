from .models import Language


def languages_processor(request):
    """Add all languages in each context"""
    languages = Language.objects.all()
    return {'languages': languages}
