from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Xrays(models.Model):
    uploadedBy = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    uploadedOn = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to = 'uploadedXrays/')
    confidence = models.FloatField(default=1)
    result = models.CharField(max_length=30)