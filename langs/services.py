from django.utils.translation import LANGUAGE_SESSION_KEY
from django.conf import settings
from django.http import HttpResponse

from utils.logs import handle_services_exceptions


@handle_services_exceptions
def set_language_session(session, language: str) -> None:
    """Set language session key for session"""
    session[LANGUAGE_SESSION_KEY] = language


@handle_services_exceptions
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
