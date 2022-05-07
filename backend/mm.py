from django.db import models
from django.contrib.aut.models import User

class Todo(models.Model):
    title = models.CharField(max_lengh=100)
    memo = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title  
