from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static

from . import views


urlpatterns = [
	url(r'^2/$', views.ApiEndpoint.as_view()),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
