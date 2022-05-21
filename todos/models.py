from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=150)
    content =  models.CharField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
