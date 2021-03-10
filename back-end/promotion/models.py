from django.db import models
import datetime


# Create your models here.
class Promotion(models.Model):
    title = models.CharField(max_length=255)
    min_seller = models.IntegerField()
    max_seller = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField(null=True)
    participants = models.ManyToManyField('Seller')

    def apply(self, seller):
        if seller in self.participants.all():
            raise ValueError('Promotion Apply: duplicate participant')
        if self.participants.count() >= self.max_seller:
            raise ValueError('Promotion Apply: fully booked')
        if self.start_date <= datetime.date.today():
            raise ValueError('Promotion Apply: expired')

        self.participants.add(seller)

    def __str__(self):
        return self.title


class Seller(models.Model):
    brand_id = models.CharField(max_length=10)

    def __str__(self):
        return self.brand_id
