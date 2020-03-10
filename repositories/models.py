from django.db import models

class Repository(models.Model):
    name = models.CharField(max_length=50)
    updated_date = models.DateTimeField()
    dependencies = models.ManyToManyField('Dependency', blank=True)

class Dependency(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name
