from django.db import models

# Create your models here.
class Contact(models.Model):
    phoneOne = models.CharField(max_length=15)
    phoneTwo = models.CharField(max_length=15)
    phoneThree = models.CharField(max_length=15)
    phoneFour = models.CharField(max_length=15)
    email = models.CharField(max_length=50 ,blank=True, null=True)
    face = models.URLField()
    inst = models.URLField()
    tele = models.URLField()
    tup = models.URLField()
    twit = models.URLField()
    workTime = models.TextField(max_length=50)
    workOff = models.TextField(max_length=50)
    about =models.TextField(max_length=100)
    adderess = models.TextField(max_length=100)
    
    def __str__(self):
        return f"{self.phoneOne}- {self.adderess}"
    
    
    
    
    
    
class UserMessage(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    phone = models.CharField(max_length=50)
    subject = models.CharField(max_length=1000)
    message = models.TextField(max_length=2800)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f" {self.name} - {self.email} - {self.date}"

    class Meta:
        verbose_name = 'message from users'
        verbose_name_plural = 'users message'