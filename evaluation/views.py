from django.shortcuts import render,get_object_or_404

from rest_framework.views import APIView
from rest_framework import authentication,permissions
from rest_framework.response import Response
from rest_framework import serializers

from exams.models import Assessment

from problem.models import Question

from evaluation.permissions import IsStudent
from evaluation.models import Submission,Answer
from evaluation.serializers import SubmissionSerializer,AnswerSerializer

class SubmissionStartView(APIView):

    authentication_classes = [authentication.BasicAuthentication]

    permission_classes = [IsStudent]

    def post(self,request,pk=None):

        assessment_id = pk

        assessment_object = get_object_or_404(Assessment,id=assessment_id)

        instance = Submission.objects.create(assessment=assessment_object,student=request.user)

        serializer_instance = SubmissionSerializer(instance)

        return Response(data=serializer_instance.data)

class AnswerCreateView(APIView):

    authentication_classes = [authentication.BasicAuthentication]

    permission_classes = [IsStudent]

    def post(self,request,pk=None):

        submission_id = pk

        submission_object = get_object_or_404(Submission,id=submission_id)

        form_data = request.data

        #-----validation start

        assessment_object = submission_object.assessment

        assessment_question = Question.objects.filter(assessment=assessment_object).values_list("id",flat=True)

        question = form_data.get("question")

        if question not in assessment_question:

            raise serializers.ValidationError("Invalid question,question not existing")


        #-------validation end

        serializer_instance = AnswerSerializer(data=form_data)

        if serializer_instance.is_valid():

            serializer_instance.save(submission=submission_object)

        return Response(data=serializer_instance.data)

class SubmissionRetrieveView(APIView):

    authentication_classes = [authentication.BasicAuthentication]

    permission_classes = [permissions.IsAdminUser]

    def get(self, request, pk=None):

        instance = get_object_or_404(Submission,id=pk)

        serializer_instance = SubmissionSerializer(instance)

        return Response(data=serializer_instance.data)

class AnswerUpdateView(APIView):

    authentication_classes = [authentication.BasicAuthentication]

    permission_classes = [permissions.IsAdminUser]


    def patch(self,request,pk=None):

        answer_id =pk

        form_data = request.data

        answer_object = get_object_or_404(Answer,id=answer_id)

        serializer_instance = AnswerSerializer(data=form_data,instance=answer_object,partial = True)

        serializer_instance.fields["marks_awarded"].read_only = False
        
        serializer_instance.fields["feedback"].read_only = False

        if serializer_instance.is_valid():

            print(serializer_instance.validated_data)

            serializer_instance.save()

            return Response(data=serializer_instance.data)


        else:

            return Response(data=serializer_instance.errors)

    



    




        



