from django.db import models
from django.contrib.auth.models import User


class JsonData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="userId")
    title = models.CharField(max_length=100)
    body = models.TextField()

    class Meta:
        db_table = "uploaded_data"
