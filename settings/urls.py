from django.conf import settings
from django.contrib import admin
from django.urls import include, path

from settings.utils import ENVS

urlpatterns = [
    path(f'{settings.API_PREFIX}/admin/', admin.site.urls),
    path(f'{settings.API_PREFIX}/cluster/', include('cluster_management.urls')),
]

if settings.ENV == ENVS.DEV:
    from drf_spectacular.views import (
        SpectacularAPIView,
        SpectacularRedocView,
        SpectacularSwaggerView,
    )

    swagger_urls = [
        path(f'{settings.API_PREFIX}/schema/', SpectacularAPIView.as_view(), name='schema'),
        path(
            f'{settings.API_PREFIX}/schema/swagger-ui/',
            SpectacularSwaggerView.as_view(url_name='schema'),
            name='swagger-ui',
        ),
        path(
            f'{settings.API_PREFIX}/schema/redoc/',
            SpectacularRedocView.as_view(url_name='schema'),
            name='redoc',
        ),
    ]
    urlpatterns += swagger_urls
