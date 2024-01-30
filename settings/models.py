from django.db import models

# Create your models here.
class Settings(models.Model):
    main_machine = models.CharField(default="loader", max_length=255)
    template_name = models.CharField(default="Loading Bay", max_length=255)
    location= models.CharField(default="HQ", max_length=255)
    contacts = models.CharField(default="02 xxx-xxxx / 02 xxx-xxxx", max_length=255)
   
    def __str__(self):
        return f'{self.main_machine}'