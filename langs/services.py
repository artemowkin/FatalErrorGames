from django.utils.translation import LANGUAGE_SESSION_KEY
from django.conf import settings
from django.http import HttpResponse

from .models import Language


def is_language_code_correct(language_code: str) -> bool:
    """Check is language code in `Language` model entries"""
    all_languages = Language.objects.all().values_list('code', flat=True)
    return language_code in all_languages


def set_language_session(session, language: str) -> None:
    """Set language session key for session"""
    session[LANGUAGE_SESSION_KEY] = language


def set_response_language_cookie(
        response: HttpResponse, language: str) -> None:
    """Set language cookie in response"""
    response.set_cookie(
        settings.LANGUAGE_COOKIE_NAME, language,
        max_age=settings.LANGUAGE_COOKIE_AGE,
        path=settings.LANGUAGE_COOKIE_PATH,
        domain=settings.LANGUAGE_COOKIE_DOMAIN,
        secure=settings.LANGUAGE_COOKIE_SECURE,
        httponly=settings.LANGUAGE_COOKIE_HTTPONLY,
        samesite=settings.LANGUAGE_COOKIE_SAMESITE,
    )
