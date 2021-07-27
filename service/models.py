from django.db import models

# Create your models here.
class Service(models.Model):
    icon = models.ImageField(upload_to='service', null=True, blank= True)
    service_name = models.CharField(max_length=50)
    description = models.TextField(max_length=80)
    
    def __str__(self):
        return f"{self.service_name}"
    
    
    