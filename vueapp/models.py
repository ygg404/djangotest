from django.db import models

# Create your models here.
class city(models.Model):
    ID = models.IntegerField(primary_key=True)
    Name = models.CharField(max_length=35)
    CountryCode = models.CharField(max_length=3)
    District = models.CharField(max_length=20)
    Population = models.IntegerField()