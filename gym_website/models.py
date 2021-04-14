from django.db import models

# Create your models here.

class ContactUs(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.name

class FreeTrial(models.Model):
    photo = models.ImageField(upload_to='media/trialPhoto/', blank=True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)

    def __str__(self):
        return self.name