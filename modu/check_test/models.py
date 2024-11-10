from django.db import models

# Create your models here.
class Chat(models.Model):
    code = models.CharField(max_length=20, unique=True, primary_key=True, editable=False)
    title = models.CharField(max_length=255,null=True,)
    added_at = models.DateTimeField(auto_now_add=True)