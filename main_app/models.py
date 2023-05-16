from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class About(models.Model):
  titel=models.CharField(max_length=30,blank=True,null=True)
  text=models.TextField(null=True)
  def __str__(self) -> str:
    return self.titel

class Profil(models.Model):
  name=models.CharField(max_length=30)
  email=models.CharField(max_length=30)
  tel=models.CharField(max_length=15,null=True,blank=True)
  uzi_malumot=models.CharField(max_length=30)
  media=models.FileField(null=True,blank=True)
  def __str__(self) -> str:
    return self.name
 
class Maqola(models.Model):
  titel=models.CharField(max_length=30,null=True)
  matn=models.TextField(null=True)
  profil=models.ForeignKey(Profil,on_delete=models.CASCADE)
  date=models.DateField(auto_now_add=True,blank=True,null=True)
  media=models.FileField(null=True,blank=True)
  def __str__(self) -> str:
    return self.titel
  