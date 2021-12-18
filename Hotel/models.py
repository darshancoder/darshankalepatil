from django.db import models

# Create your models here.
class Customer(models.Model):
      cusid = models.IntegerField()
      cusname = models.TextField(max_length=30)
      cusmail = models.EmailField(max_length=30)
      cuspass = models.TextField(max_length=30)
      
      def __str__(self):
          return self.cusname

class Contact(models.Model):
      name= models.TextField(max_length=30)
      email=models.EmailField(max_length=30)
      subject=models.TextField(max_length=30)
      message=models.TextField(max_length=80)

      def __str__(self):
          return self.name            