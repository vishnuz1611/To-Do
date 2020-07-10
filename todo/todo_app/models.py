from django.db import models

# Create your models here.
class Tasks(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    complete = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title