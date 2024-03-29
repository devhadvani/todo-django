from django.db import models

# Create your models here.
class Todo(models.Model):
    name = models.CharField(max_length=60)
    complete = models.BooleanField(null=True)

    def __str__(self):
        return self.name