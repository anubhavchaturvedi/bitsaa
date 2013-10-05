from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserData(models.Model):
  username=models.ForeignKey(User)
  bits_id=models.CharField(max_length=12,unique=True)
  name=models.CharField(max_length=50)
  dob=models.DateField()
  address=models.CharField(max_length=50)
  mobile=models.CharField(max_length=15)
  about_me=models.TextField(default="")
  
  def __unicode__(self):
    return self.name+' ( '+self.bits_id+' )'
