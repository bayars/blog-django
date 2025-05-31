from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from posts.views import PostViewSet
from projects.views import ProjectViewSet
from gallery.views import AlbumViewSet, PhotoViewSet
from resume.views import ProfileViewSet

router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'projects', ProjectViewSet)
router.register(r'albums', AlbumViewSet)
router.register(r'photos', PhotoViewSet)
router.register(r'profile', ProfileViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('posts.urls')),
    path('api/', include('projects.urls')),
    path('api/', include('gallery.urls')),
    path('api/', include('resume.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 