from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from user.ViewSet import UserViewSet
from entry.ViewSet import EntryViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'api/entry', EntryViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
