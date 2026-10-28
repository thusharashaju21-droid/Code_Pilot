from django.shortcuts import render,get_object_or_404

from rest_framework.views import APIView
from rest_framework import authentication
from rest_framework.response import Response

from exams.models import Assessment

from evaluation.permissions import IsStudent
from evaluation.models import Submission
from evaluation.serializers import SubmissionSerializer,AnswerSerializer

class SubmissionStartView(APIView):

    authentication_classes = [authentication.BasicAuthentication]

    permission_classes = [IsStudent]

    def post(self,request,pk=None):

        assessment_id = pk

        assessment_object = get_object_or_404(Assessment,id=assessment_id)

        instance = Submission.objects.create(assessment=assessment_object,student=request.user)

        serializer_instance = SubmissionSerializer(instance)

        return Response(serializer_instance.data)

class AnswerCreateView(APIView):

    authentication_classes = [authentication.BasicAuthentication]

    permission_classes = [IsStudent]

    def post(self,request,pk=None):

        submission_id = pk

        submission_object = get_object_or_404(Submission,id=submission_id)

        form_data = request.data

        serializer_instance = AnswerSerializer(data=form_data)

        if serializer_instance.is_valid():

            serializer_instance.save(submission=submission_object)

        return Response(data=serializer_instance.data)




        



