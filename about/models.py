from django.db import models

# Create your models here.
CATEGORY = [
    ('ONE','one'),
    ('TOW','tow'),
    ('THREE','three'),
    ('NON','non'),
]


class About(models.Model):
    title = models.CharField(max_length=150 , null=True, blank=True)
    intro = models.TextField(max_length=1000 , null=True, blank=True)
    body = models.TextField(max_length=5000 , null=True, blank=True)
    image = models.ImageField(upload_to='about',null=True,blank=True)
    link = models.URLField(null=True,blank=True)
    category = models.CharField(max_length=5, choices=CATEGORY)
    
    def  __str__(self):
         return f"{self.title} - {self.category}"
     
class Why(models.Model):
    title = models.CharField(max_length=50, null=True, blank=True)
    hint = models.TextField(max_length=700, null=True, blank=True)
    benifit = models.CharField(max_length=50, null=True, blank=True)
    image = models.ImageField(upload_to='about/why', blank=True, null=True)
    
    
    def __str__(self):
        return f"{self.title}"
    
class Team(models.Model):
    job = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    body = models.TextField(max_length=500)
    image = models.ImageField(upload_to='about/team', null=True, blank=True)
    face = models.URLField(null=True, blank=True)
    inst = models.URLField(null=True, blank=True)
    tele = models.URLField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.name} - {self.job}"