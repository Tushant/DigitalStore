from django.conf.urls.static import static
from django.conf.urls import include, url
from django.conf import settings
from django.contrib import admin

urlpatterns = [
    url(r'^', include('pages.urls', namespace='pages')),
    url(r'^', include('Store.urls', namespace='store')),
    url(r'^api/v1/', include('Store.urls', namespace='store-api')),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
