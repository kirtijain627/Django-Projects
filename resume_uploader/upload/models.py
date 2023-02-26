from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Resume(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    resume = models.FileField(upload_to = 'resumes/')
    
    
    def __str__(self):
        return self.user.username