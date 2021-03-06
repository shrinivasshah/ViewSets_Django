from django.shortcuts import render
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated]

    # def list(self, request):
    #     stu = Student.objects.all()
    #     serializer = StudentSerializer(stu, many=True)
    #     return Response(serializer.data)

    # def retrieve(self, request, pk=None):
    #     id = pk
    #     if id is not None:
    #         stu = Student.objects.get(id=id)
    #         serializer = StudentSerializer(stu)
    #         return Response(serializer.data)

    # def create(self, request):
    #     serializer = StudentSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response({"msg": "Data Created"}, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    # def update(self, request, pk):
    #     id = pk
    #     stu = Student.Object.get(pk=id)
    #     serializer = StudentSerializer(stu, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response({"msg": "Data Updated"})
    #     return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    # def partial_update(self, request, pk):
    #     id = pk
    #     stu = Student.objects.get(pk=id)
    #     serializer = StudentSerializer(stu, request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response({"msg": "Data Partially updated"})
    #     return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    # def destroy(self, request, pk):
    #     id = pk
    #     stu = Student.objects.get(pk=id)
    #     stu.delete()
    #     return Response({"msg": "Data Deleted"})
