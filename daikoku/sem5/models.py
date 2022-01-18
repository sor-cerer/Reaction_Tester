from django.db import models
from django.db.models.fields.related import ForeignKey
from django.contrib.auth.models import User

# Create your models here.

class uscore(models.Model):
    index = models.AutoField (primary_key=True )
    username_id = models.ForeignKey (User,  on_delete = models.CASCADE,default="" )
    lvl = models.CharField(max_length=40, default="warm_up")    
    best = models.FloatField(default="", editable="false")
    avg = models.FloatField(default="", editable="false") 

