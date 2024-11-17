from django.shortcuts import render
from .serializers import Subject, SubjectSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

class All_subjects(APIView):
    def get(self, request):
        subjects = Subject.objects.all()
        serialized_subjects = SubjectSerializer(subjects, many=True)
        return Response(serialized_subjects.data)
