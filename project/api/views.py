from django.shortcuts import render
from django.shortcuts import render
from rest_framework.authentication import SessionAuthentication,BasicAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializers import SchoolSerializer,StudentSerializer
from rest_framework import viewsets
from rest_framework import status
from rest_framework.authtoken.models import Token

# Create your views here.
class SchoolViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = SchoolModel.objects.all()
    serializer_class = SchoolSerializer


class StudentViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = StudentModel.objects.all()
    serializer_class = StudentSerializer
