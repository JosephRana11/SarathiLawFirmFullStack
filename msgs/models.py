from django.db import models

# Create your models here.
class Contact_Message(models.Model):
  msg = models.TextField()
  email = models.EmailField(max_length=254 , null = True)
  phone_number = models.CharField( max_length=50)
  date = models.DateTimeField(auto_now_add=True)