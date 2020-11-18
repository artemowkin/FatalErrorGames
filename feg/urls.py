from django.contrib import admin
from django.urls import path, include, register_converter
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    # Django Admin
    path('admin/', admin.site.urls),

    # TinyMCE
    path('tinymce/', include('tinymce.urls')),

    # Local
    path('', include('pages.urls')),
    path('langs/', include('langs.urls')),
    path('project/', include('persons.urls')),
    path('games/', include('games.urls')),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
