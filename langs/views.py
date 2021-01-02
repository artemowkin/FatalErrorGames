import json

from django.shortcuts import render
from django.http import JsonResponse, Http404
from django.conf import settings
from django.views.decorators.http import require_http_methods

from . import services


@require_http_methods(["POST"])
def set_language(request):
    if not request.content_type == 'application/json':
        raise Http404

    language = json.loads(request.body).get(
        'language', settings.LANGUAGE_CODE
    )
    if not services.is_language_code_correct(language):
        language = settings.LANGUAGE_CODE

    if request.user.is_authenticated:
        services.set_language_session(request.session, language)

    response = JsonResponse({'status': 'ok'})
    services.set_response_language_cookie(response, language)
    return response
