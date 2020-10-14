from django.views import View
from django.shortcuts import render
from django.http import Http404
from django.conf import settings
from django.http import HttpRequest, HttpResponse


class DefaultView(View):

    """View with exceptions handling

    Methods
    -------
    dispatch(request, *args, **kwargs)
        Handle request

    """

    def dispatch(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        """
        Try to handle request. Render 404.html if 404 error
        or error.html if something went wrong
        """
        try:
            return super().dispatch(request, *args, **kwargs)
        except Http404:
            raise
        except Exception:
            if settings.DEBUG:
                raise

            return render(request, 'error.html')

