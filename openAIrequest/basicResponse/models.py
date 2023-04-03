from django.db import models

# Create your models here.

class Answer(models.Model):
    question = models.TextField()
    AIanswer = models.TextField(blank=True)
    
class PersonalInfo(models.Model):
    first_name= models.CharField(max_length=30)
    last_name= models.CharField(max_length=30)
    date_of_birth= models.DateField()
    phone_number = models.CharField(max_length=20)
    address_line = models.TextField()
    email_addres = models.EmailField()
    biography = models.TextField()
    