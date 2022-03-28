from django.db import models


class ParsedDocument(models.Model):
    title = models.CharField(max_length=255)
    link = models.CharField(max_length=255)
