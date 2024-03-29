import logging

from django.views import View
from django.http import Http404
from django.http import HttpRequest, HttpResponse


logger = logging.getLogger('filelogger')


class DefaultView(View):
    """View with exceptions handling

    Methods
    -------
    dispatch(request, *args, **kwargs)
        Handle request

    """

    def dispatch(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        """
        Handle exceptions and log problems
        """
        try:
            return super().dispatch(request, *args, **kwargs)
        except Http404:
            logger.warning(f"404 Not Found on {request.path}")
            raise
        except Exception:
            logger.exception(f"Problem with request on {request.path}")
            raise
