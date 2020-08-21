from django.db import models

# Create your models here.

class Currency(models.Model):

    currency_name=models.CharField(max_length=100)
    buying_currency=models.FloatField()
    selling_currency=models.FloatField()
    difference=models.FloatField()
    currency_code=models.CharField(max_length=100) #USD/TR

def __str__(self):
    return self.currency_name
    


