from django.db import models

# Create your models here.

class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(150)
    content = models.TextField(null=True)
    created_at = models.DateTimeField(null=True)
    updated = models.DateTimeField(null=True)
    deleted_at = models.DateTimeField(null=True)


