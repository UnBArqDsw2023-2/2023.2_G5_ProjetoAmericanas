import uuid

from django.db import models


class Base(models.Model):
    id = models.CharField(primary_key=True, default=uuid.uuid4, max_length=40)
    dt_criacao = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True