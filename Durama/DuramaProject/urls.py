from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import RegisterView,verify_otp


urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Obtenir le token
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'), # Rafraîchir le token
    path('register/', RegisterView.as_view(), name='register'),
    path("jwt/create/",TokenObtainPairView.as_view(),name="jwt-create"),
    path('verify_otp/', verify_otp, name='verification otp'),
]