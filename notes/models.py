from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#this creates a model in the database, it won't show until you add it to

class Notes(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name ="notes")