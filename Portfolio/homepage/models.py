from django.db import models

# Create your models here.


class HomePage(models.Model):

    header_image = models.ImageField(
        null=True, blank=True, upload_to='images/')
    navigation1 = models.CharField(max_length=100, null=True, blank=True)
    navigation2 = models.CharField(max_length=100, null=True, blank=True)

    herotitle = models.TextField(null=True, blank=True)
    herotext1 = models.TextField(null=True, blank=True)
    herotext2 = models.TextField(null=True, blank=True)
    hero_image = models.ImageField(
        null=True, blank=True, upload_to='images/')
    middletitle = models.CharField(max_length=100, null=True, blank=True)
    middletext = models.TextField(null=True, blank=True)
    middletitle1 = models.CharField(max_length=100, null=True, blank=True)
    middletext1 = models.TextField(null=True, blank=True)
    endtext = models.CharField(max_length=100, null=True, blank=True)
    endemail = models.CharField(max_length=100, null=True, blank=True)
    contactme = models.CharField(max_length=100, null=True, blank=True)
    footerheading = models.CharField(max_length=100, null=True, blank=True)
    footer1 = models.CharField(max_length=100, null=True, blank=True)
    footer2 = models.CharField(max_length=100, null=True, blank=True)
    footer3 = models.CharField(max_length=100, null=True, blank=True)
