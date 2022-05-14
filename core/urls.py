from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls', namespace='index')),
    path('page/', include('pages.urls', namespace='pages')),
    path('account/', include('accounts.urls', namespace='accounts')),
    path('toy/', include('toys.urls', namespace='toys')),
    path('basket/', include('basket.urls', namespace='basket')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
