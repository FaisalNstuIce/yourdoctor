from django.db import models 
from users.models import CustomUser,UserInfo







class DoctorInfo(models.Model):

    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE )
    # Medical basic Information
    bmdc_number = models.CharField(max_length=30,null=True,blank=True)
    current_position = models.CharField(max_length=50,null=True,blank=True)
    current_working_department = models.CharField(max_length=200,null=True,blank=True)
    current_working_institution = models.CharField(max_length=200,null=True,blank=True)
    

    def __str__(self):
        return self.user.email

class Speciality(models.Model):
    
    user       = models.ForeignKey(CustomUser,on_delete=models.CASCADE,null=True)
    speciality = models.CharField(max_length=50,null=True,blank=True)
    speciality_details = models.CharField(max_length=400,null=True,blank=True)

class Experience(models.Model):

    user       = models.ForeignKey(CustomUser,on_delete=models.CASCADE,null=True)
    exp_name   = models.CharField(max_length=200,null=True,blank=True)
    exp_details   = models.CharField(max_length=500,null=True,blank=True)
    