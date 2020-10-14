from django.contrib import admin
from django.urls import path, include, register_converter
from django.conf import settings
from django.conf.urls.static import static

from utils.urls import LanguageConverter


register_converter(LanguageConverter, 'language')

urlpatterns = [
    # Django Admin
    path('admin/', admin.site.urls),

    # TinyMCE
    path('tinymce/', include('tinymce.urls')),

    # Local
    path('', include('pages.urls')),
    path('<language:lang>/project/', include('persons.urls')),
    path('<language:lang>/games/', include('games.urls')),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
