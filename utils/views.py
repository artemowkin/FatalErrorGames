from django.views import View
from django.shortcuts import render
from django.http import Http404
from django.core.exceptions import ImproperlyConfigured
from django.conf import settings


class DefaultView(View):

    """View with errors exception"""

    def dispatch(self, request, *args, **kwargs):
        try:
            return super().dispatch(request, *args, **kwargs)
        except (Http404, ImproperlyConfigured):
            raise
        except Exception:
            if settings.DEBUG:
                raise

            return render(request, 'error.html')

