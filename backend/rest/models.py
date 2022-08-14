from django.db import models

# Create your models here.


class Project(models.Model):
    name = models.CharField(max_length=50)
    tag = models.CharField(unique=True, max_length=3)
    description = models.TextField()
    project_owner = models.CharField(max_length=50)

    def __str__(self):
        return "%s" % (self.name)


class TestSet(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return "%s - %s" % (self.project.tag, self.name)


class TestCase(models.Model):
    test_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.TextField()
    test_set = models.ForeignKey(TestSet, on_delete=models.CASCADE)

    def __str__(self):
        return "%s-%s" % (self.test_set.project.tag, str(self.test_id))


class Environment(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return "%s" % (self.name)


class TestExecution(models.Model):
    test_case = models.ForeignKey(TestCase, on_delete=models.CASCADE)
    success = models.BooleanField()
    environment = models.ForeignKey(
        Environment,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    error_code = models.TextField()
    start_time = models.DateTimeField()
    finish_time = models.DateTimeField()
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s - %s" % (self.test_case, str(self.success))
