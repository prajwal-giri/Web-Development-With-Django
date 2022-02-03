from django.db import models

# Create your models here.


class Cblog(models.Model):
    title = models.CharField(max_length=50, null=True, blank=True)
    body = models.TextField(null=True, blank=True)
    intro = models.CharField(max_length=200, null=True, blank=True)
    blogimage = models.ImageField(
        null=True, blank=True, upload_to='images/')

    def __str__(self):
        return self.title
