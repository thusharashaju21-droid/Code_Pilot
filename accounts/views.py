from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from accounts.serializers import UserSerializers
from accounts.models import User
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

