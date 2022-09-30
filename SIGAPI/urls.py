from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static


from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('SIGAPI_rest/', include("SIGAPI_rest.urls"))
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
