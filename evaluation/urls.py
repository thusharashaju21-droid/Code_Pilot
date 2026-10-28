
from django.urls import path
from evaluation.views import SubmissionStartView,AnswerCreateView

urlpatterns = [

    path("assessment/<int:pk>/submission/", SubmissionStartView.as_view()),
    path("submission/<int:pk>/answer/",AnswerCreateView.as_view()),
]

