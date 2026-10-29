
from django.urls import path
from evaluation.views import SubmissionStartView,AnswerCreateView,SubmissionRetrieveView

urlpatterns = [

    #Submission Start View
    path("assessment/<int:pk>/submission/", SubmissionStartView.as_view()),

    #Answer Create View
    path("submission/<int:pk>/answer/",AnswerCreateView.as_view()),

    #Submission Retrieve View
    path("submission/<int:pk>/", SubmissionRetrieveView.as_view()),
]

