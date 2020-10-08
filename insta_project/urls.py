from django.contrib import admin
from django.conf import settings 
from django.urls import path, include 
from django.conf.urls.static import static 

from rest_framework import routers
from imagerepo import views


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet) # Add routes for APIs
router.register(r'groups', views.GroupViewSet)
router.register(r'imageviews', views.ImageViewViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('imagerepo.urls')),    # Include routes for our main app
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

admin.site.site_header = "Image Repo Challenge"

if settings.DEBUG: 
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)