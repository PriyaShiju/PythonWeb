from django.db import models
from datetime import datetime

# Create your models here.
class Caste(models.Model):
    caste_name = models.CharField("Caste", max_length=25)
    caste_code = models.CharField(("Caste Code"), max_length=50)
    
    def __str__(self):
        return f"{self.caste_code} - {self.caste_name}"
    
class Religion(models.Model):
    reli_name = models.CharField("Religion",max_length=25)
    reli_code = models.CharField(("Religion Code"), max_length=50)
    
    def __str__(self):
        return f"{self.reli_code} - {self.reli_name}"
    
class Users(models.Model):
    Name = models.CharField(max_length=200)
    DOB = models.DateField()
    EMailId = models.CharField(max_length=50)
    PhoneNumber = models.IntegerField(default=1)
    religion = models.ForeignKey(Religion,on_delete=models.CASCADE)
    caste = models.ForeignKey(Caste,on_delete=models.CASCADE)
    
    def __str__(self):
        return f"Name : {self.Name} , Age: {self.DOB} , Caste: {self.caste}, EMailId : {self.EMailId}"