from django.db import models

# Create your models here.

class Answer(models.Model):
    question = models.TextField()
    AIanswer = models.TextField(blank=True)
    
class GeneralInfo(models.Model):
    first_name= models.CharField