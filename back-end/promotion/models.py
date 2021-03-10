from django.db import models, transaction
import datetime


# Create your models here.
class Promotion(models.Model):
    title = models.CharField(max_length=255)
    min_seller = models.IntegerField()
    max_seller = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField(null=True)
    participants = models.ManyToManyField('Seller')

    def _apply(self, seller):
        existing_participant = self.participants.all()

        if seller in existing_participant:
            raise ValueError('Promotion Apply: duplicate participant')
        if existing_participant.__len__() >= self.max_seller:
            raise ValueError('Promotion Apply: fully booked')
        if self.start_date <= datetime.date.today():
            raise ValueError('Promotion Apply: expired')

        self.participants.add(seller)

        return self

    @classmethod
    @transaction.atomic
    def apply(cls, id, seller):
        promotion = cls.objects.select_for_update().get(id=id)

        return promotion._apply(seller)

    def __str__(self):
        return self.title


class Seller(models.Model):
    brand_id = models.CharField(max_length=10, unique=True, db_index=True)

    def __str__(self):
        return self.brand_id
