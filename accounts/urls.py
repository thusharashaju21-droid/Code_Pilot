from django.urls import path
from accounts.views import AdminCreateView
from accounts.views import StudentCreateView

urlpatterns = [
    path("register/",AdminCreateView.as_view()),
    path("student/",StudentCreateView.as_view()),
]