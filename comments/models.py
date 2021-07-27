from django.db import models

# Create your models here.
class Comments(models.Model):
    image = models.ImageField(upload_to='comments', null=True , blank= True)
    body = models.TextField(max_length=700, null=True , blank=True)
    starts = models.TextField(null=True ,blank=True)
    name = models.CharField(max_length=25, null=True, blank=True)
    job = models.CharField(max_length=25)
    
    def __str__(self):
        return f"{self.name} - {self.job}"
    