
from django.urls import path
from evaluation.views import SubmissionStartView
from evaluation.views import AnswerCreateView
from evaluation.views import SubmissionRetrieveView
from evaluation.views import AnswerUpdateView

urlpatterns = [

    #Submission Start View
    path("assessment/<int:pk>/submission/", SubmissionStartView.as_view()),

    #Answer Create View
    path("submission/<int:pk>/answer/",AnswerCreateView.as_view()),

    #Submission Retrieve View
    path("submission/<int:pk>/", SubmissionRetrieveView.as_view()),

    #Answer Evaluate View
    path("answers/<int:pk>/",AnswerUpdateView.as_view()),
]

