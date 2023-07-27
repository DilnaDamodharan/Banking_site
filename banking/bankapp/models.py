from django.db import models
from django.db.models.deletion import CASCADE


# Create your models here.
class District(models.Model):
    name = models.CharField(max_length=100)
    wikilink = models.URLField(max_length=250)

    def __str__(self):
        return self.name


class Branch(models.Model):
    distid = models.ForeignKey(District, on_delete=CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
