from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework_simplejwt.authentication import JWTAuthentication 

from accounts.serializers import UserSerializers,StudentProfileSerializer
from accounts.models import User,StudentProfile

from evaluation.permissions import  IsStudent

# Create your views here.
class AdminCreateView(APIView):

    def post(Self,request):

        form_data = request.data

        serializer_instance=UserSerializers(data=form_data)

        if serializer_instance.is_valid():

            cleaned_data = serializer_instance.validated_data

            instance = User.objects.create_superuser(role="admin",**cleaned_data)

            #save()- no password encrpt ,role=student

            serializer_instance=UserSerializers(instance)

            return Response(data=serializer_instance.data)

        else:

            return Response(data=serializer_instance.errors)

class StudentCreateView(APIView):

    def post(self,request):

        form_data = request.data

        serializer_instance = UserSerializers(data=form_data)

        if serializer_instance.is_valid():

            cleaned_data = serializer_instance.validated_data

            instance = User.objects.create_user(role="student",**cleaned_data)

            serializer_instance=UserSerializers(instance)

            return Response(data=serializer_instance.data)

        else:

            return Response(data=serializer_instance.errors)

class ProfileUpdateView(APIView):

    authentication_classes = [JWTAuthentication]

    permission_classes = [permissions.IsAuthenticated,IsStudent]

    def put(self,request):

        form_data = request.data

        student_profile_object = StudentProfile.objects.get(student=request.user)

        serializer_instance = StudentProfileSerializer(data=form_data,instance=student_profile_object)

        if serializer_instance.is_valid():

            serializer_instance.save()

            return Response(data=serializer_instance.data)

        else:

            return Response(data=serializer_instance.errors)


class StudentProfileMeView(APIView):

    authentication_classes = [JWTAuthentication]

    permission_classes = [permissions.IsAuthenticated, IsStudent]

    def get(self, request):

        student_profile_object = StudentProfile.objects.get(student=request.user)

        serializer_instance = StudentProfileSerializer(student_profile_object)

        return Response(data=serializer_instance.data)
