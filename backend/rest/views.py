from django.contrib.auth.models import User, Group

from rest_framework import viewsets
from rest_framework import generics
from rest_framework import permissions


from .models import Project, TestCase, TestSet, Environment, TestExecution
from .serializers import UserSerializer, GroupSerializer, ProjectSerializer, TestSetSerializer, TestCaseSerializer, EnvironmentSerializer, TestExecutionSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated]


class TestSetViewSet(viewsets.ModelViewSet):
    queryset = TestSet.objects.all()
    serializer_class = TestSetSerializer
    permission_classes = [permissions.IsAuthenticated]


class TestCaseViewSet(viewsets.ModelViewSet):
    queryset = TestCase.objects.all()
    serializer_class = TestCaseSerializer
    permission_classes = [permissions.IsAuthenticated]


class EnvironmentViewSet(viewsets.ModelViewSet):
    queryset = Environment.objects.all()
    serializer_class = EnvironmentSerializer
    permission_classes = [permissions.IsAuthenticated]


class TestExecutionViewSet(viewsets.ModelViewSet):
    queryset = TestExecution.objects.all()
    serializer_class = TestExecutionSerializer
    permission_classes = [permissions.IsAuthenticated]
