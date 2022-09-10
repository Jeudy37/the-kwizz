from django.db import models

# Create your models here.
from django.contrib.auth.models import User


class Quiz(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    question=models.CharField(max_length=200)
    forepons1=models.CharField(max_length=300 ,blank=True, null=True)
    forepons2=models.CharField(max_length=300 ,blank=True, null=True)
    forepons3=models.CharField(max_length=300 ,blank=True, null=True)
    vre_repons=models.CharField(max_length=300 ,blank=True, null=True)


    class Meta:
        verbose_name = ' a Quiz'
        verbose_name_plural = 'Quiz'

    
    def __str__(self):
        return self.question

