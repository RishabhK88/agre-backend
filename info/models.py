from django.db import models

# Create your models here.
class Data(models.Model):
    type = models.CharField(max_length = 200)
    health = models.CharField(max_length = 200)
    temperature = models.CharField(max_length = 200)
    moisture = models.CharField(max_length = 200)
    nitrogen = models.CharField(max_length = 200)
    phosphorus = models.CharField(max_length = 200)
    potassium = models.CharField(max_length = 200)
    def __str__(self):
        return self.type