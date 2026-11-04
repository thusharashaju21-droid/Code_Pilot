from django.urls import path
from accounts.views import AdminCreateView
from accounts.views import StudentCreateView
from accounts.views import ProfileUpdateView
from accounts.views import StudentProfileMeView

from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path("admin/register/",AdminCreateView.as_view()),
    path("student/register",StudentCreateView.as_view()),
    path("jwt/token/",TokenObtainPairView.as_view()),
    path("jwt/token/refresh/",TokenRefreshView.as_view()),
    path("profile/update/",ProfileUpdateView.as_view()),
    path('profile/me/', StudentProfileMeView.as_view()),
]