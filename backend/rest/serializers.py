from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Project, TestSet, TestCase, Environment, TestExecution


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = [
            'id',
            'name',
            'tag',
            'description',
            'project_owner'
        ]


class TestSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestSet
        fields = [
            'name',
            'description',
            'project',
        ]


class TestCaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestCase
        fields = [
            'test_id',
            'name',
            'description',
            'test_set'
        ]


class EnvironmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Environment
        fields = [
            'name'
        ]


class TestExecutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestExecution
        fields = [
            'test_case',
            'success',
            'environment',
            'error_code',
            'start_time',
            'finish_time',
            'created_time',
        ]
