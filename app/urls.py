from django.urls import path
from .views import register_user, user_profile
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.urls import path


urlpatterns = [
    path('register/', register_user, name='register_user'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('profile/', user_profile, name='user_profile'),
    
    ]

