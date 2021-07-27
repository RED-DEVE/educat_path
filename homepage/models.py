from django.db import models

# Create your models here.


class welcome(models.Model):
    title = models.TextField(max_length=50)
    hint = models.TextField(max_length=70)
    word = models.CharField(max_length=20)
    HighLight = models.CharField(max_length=20)
    image = models.ImageField(upload_to='welcome_page', null=True, blank=True)

    def __str__(self):
        return f"{self.title} - {self.HighLight}"
