from django.contrib import admin
from .models import Project, TestSet, TestCase, Environment, TestExecution

# Register your models here.

admin.site.register(Project)
admin.site.register(TestSet)
admin.site.register(TestCase)
admin.site.register(Environment)
admin.site.register(TestExecution)
