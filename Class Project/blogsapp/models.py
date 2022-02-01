from django.db import models
from django.urls import reverse

# Create your models here.


class Cblogs(models.Model):
    title = models.CharField(max_length=100, null=True)
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    text = models.TextField()
    developer = models.CharField(max_length=100, null=True)
    body = models.CharField(max_length=250, null=True)
    header_image = models.ImageField(
        null=True, blank=True, upload_to='images/')

    def get_absolute_url(self):
        return reverse('blogdetail', args=[str(self.id)])

    def __str__(self):
        return self.title
