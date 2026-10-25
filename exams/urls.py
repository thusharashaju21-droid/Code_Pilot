
from django.urls import path

from rest_framework.authtoken.views import ObtainAuthToken
from exams.views import AssessmentListView,AssessmentCreateView,AssessmentRetrieveUpdateDeleteView

urlpatterns = [

    #  token authentication
    path("assessment/token/",ObtainAuthToken.as_view()),   

    # assessment list view
    path("assessment/all/",AssessmentListView.as_view()),

    #  assessment create view
    path("assessment/add/",AssessmentCreateView.as_view()),

    # assessment retrieve,update,delete view
    path("assessment/<int:pk>/",AssessmentRetrieveUpdateDeleteView.as_view()),
]