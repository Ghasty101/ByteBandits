from django.db import models


# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField()
    phone = models.CharField(max_length=10)

    def __str__(self):
        return self.name
