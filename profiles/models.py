from django.db import models
from django.contrib.auth import get_user_model
# from company.models import Company
# Create your models here.

User = get_user_model()

class GeneralUserProflie(models.Model):
    user                        = models.ForeignKey(User, on_delete=models.CASCADE, related_name='general_user_profile')
    firstName                   = models.CharField(max_length=25)
    lastName                    = models.CharField(max_length=25)
    gender                      = models.CharField(max_length=6)
    address                     = models.TextField()
    phoneNumber                 = models.CharField(max_length=25, default='+263 xxx xxx xxxx')
    profile_image               = models.ImageField(max_length=255, upload_to='static/profileImages',null=True, blank=True)

    def __str__(self):
        return f"{self.firstName} {self.lastName} (User: {self.user.username})"


# class CompanyUserProfile(models.Model):
#     user                        = models.ForeignKey(User, on_delete=models.CASCADE, related_name='company_user_profile')
#     firstName                   = models.CharField(max_length=25)
#     lastName                    = models.CharField(max_length=25)
#     gender                      = models.CharField(max_length=6)
#     phoneNumber                 = models.CharField(max_length=15, default='+263 xxx xxx xxxx')
#     company                     = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='user_company')
#     role                        = models.CharField(max_length=30)
#     profile_image               = models.ImageField(max_length=255, upload_to='static/profileImages',null=True, blank=True)

