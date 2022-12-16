from django.db import models


class Message(models.Model):
    text = models.TextField(verbose_name='Text')
    created_at = models.DateTimeField(verbose_name='Message receipt time', auto_now=True)

