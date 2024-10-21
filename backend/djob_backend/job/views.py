from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status , authentication, permissions

from .models import Job ,Category
from .serializers import JobSerializer, JobDetailSerializer ,CategorySerializer

class CategoriesView(APIView):
    def get(self, request, format=None):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        
        return Response(serializer.data)


class NewestJobsView(APIView):
    def get(self, request, format=None):
        jobs = Job.objects.all()[0:4]
        serializer = JobSerializer(jobs, many=True)
        
        return Response(serializer.data)
    

class BrowseJobsView(APIView):
    def get(self, request, format=None):
        jobs = Job.objects.all()
        serializer = JobSerializer(jobs, many=True)
        
        return Response(serializer.data)


class JobsDetailView(APIView):
    def get(self, request, pk, format=None):
        job = Job.objects.get(pk=pk)
        serializer = JobDetailSerializer(job)
        
        return Response(serializer.data)
