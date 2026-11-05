from django.urls import path
from accounts.views import AdminCreateView
from accounts.views import StudentCreateView
from accounts.views import ProfileUpdateView
from accounts.views import StudentProfileGetView

from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    #admin register view
    path("admin/register/",AdminCreateView.as_view()),

    #student register view
    path("student/register/",StudentCreateView.as_view()),

    #create jwt token
    path("jwt/token/",TokenObtainPairView.as_view()),

    #refresh jwt token
    path("jwt/token/refresh/",TokenRefreshView.as_view()),

    #profile update
    path("profile/update/",ProfileUpdateView.as_view()),

    #profile retrieve
    path('profile/me/',StudentProfileGetView.as_view()),
]