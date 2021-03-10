from django.db import models

# Create your models here.
class Promotion(models.Model):
    title = models.CharField(max_length=255)
    min_seller = models.IntegerField()
    max_seller = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField(null=True)

class Seller(models.Model):
    brand_id = models.CharField(max_length=10)
