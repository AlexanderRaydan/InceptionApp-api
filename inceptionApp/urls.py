
from django.contrib import admin
from django.urls import path , include
from django.conf.urls.static import static
from django.conf import settings


from rest_framework import routers

from api.views import InceptionImagesViewSet , Inception



route = routers.DefaultRouter()
route.register('images' , InceptionImagesViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/' , include(route.urls)),
    path('api/inception/<str:id>' , Inception )
] + static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)
