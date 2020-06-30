from django.conf import settings
from django.db import models

# Create your models here.

from django.db import models


class CustomText(models.Model):
    jhjkh = models.BigIntegerField(null=True, blank=True,)
    jhgjhgj = models.BigIntegerField(null=True, blank=True,)
    titlen = models.BigIntegerField(null=True, blank=True,)

    def __str__(self):
        return self.title

    @property
    def api(self):
        return f"/api/v1/customtext/{self.id}/"

    @property
    def field(self):
        return "title"


class HomePage(models.Model):
    body = models.TextField()

    @property
    def api(self):
        return f"/api/v1/homepage/{self.id}/"

    @property
    def field(self):
        return "body"


class Gkjhhkj(models.Model):
    "Generated Model"
    hghghg = models.UUIDField()
