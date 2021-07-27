from django.db import models

# Create your models here.
CATEGORY = [
    ('ONE','one'),
    ('TOW','tow'),
    ('THREE','three'),
    ('FOUR','four'),
    ('FIVE','five'),
]



class Students(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='students', null=True, blank=True)
    body =models.TextField(max_length=1000)
    category = models.CharField(max_length=5, choices=CATEGORY)
    
    def  __str__(self):
         return f"{self.title} - {self.category}"