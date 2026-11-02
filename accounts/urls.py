from django.urls import path
from accounts.views import AdminCreateView
from accounts.views import StudentCreateView

from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path("register/",AdminCreateView.as_view()),
    path("student/",StudentCreateView.as_view()),
    path("jwt/token/",TokenObtainPairView.as_view()),
    path("jwt/token/refresh/",TokenRefreshView.as_view()),
]