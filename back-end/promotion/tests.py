from django.test import TestCase
import datetime

from .models import Promotion, Seller


# Create your tests here.
class PromotionModelTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        for brand_id in ['A', 'B', 'C']:
            Seller.objects.create(brand_id=brand_id)

    def setUp(self):
        today = datetime.date.today()
        tomorrow = today + datetime.timedelta(days=1)

        Promotion.objects.create(title='Can Apply', min_seller=1, max_seller=3, start_date=tomorrow)
        Promotion.objects.create(title='Expired', min_seller=1, max_seller=3, start_date=today)
        promotion = Promotion.objects.create(title='Fully Booked', min_seller=1, max_seller=3, start_date=tomorrow)
        promotion.participants.set(Seller.objects.all()[:3])

    def test_given_valid_application_then_add_participant(self):
        promotion = Promotion.objects.get(title='Can Apply')
        self.assertEqual(promotion.participants.count(), 0)

        seller = Seller.objects.get(brand_id='A')
        promotion.apply(seller)
        self.assertEqual(promotion.participants.count(), 1)

    def test_given_duplicate_application_then_apply_fails(self):
        promotion = Promotion.objects.get(title='Can Apply')
        seller = Seller.objects.get(brand_id='A')
        promotion.apply(seller)
        self.assertEqual(promotion.participants.count(), 1)

        promotion.apply(seller)
        with self.assertRaises(ValueError, msg='duplicate participant'):
            promotion.apply(seller)
            self.assertEqual(promotion.participants.count(), 1)

    def test_when_promotion_expired_then_apply_fails(self):
        promotion = Promotion.objects.get(title='Expired')
        self.assertEqual(promotion.participants.count(), 0)

        seller = Seller.objects.get(brand_id='A')
        with self.assertRaises(ValueError, msg='expired'):
            promotion.apply(seller)
            self.assertEqual(promotion.participants.count(), 0)

    def test_when_promotion_fully_booked_then_apply_fails(self):
        promotion = Promotion.objects.get(title='Fully Booked')
        self.assertEqual(promotion.participants.count(), 3)

        seller = Seller.objects.create(brand_id='D')
        with self.assertRaises(ValueError, msg='fully booked'):
            promotion.apply(seller)
            self.assertEqual(promotion.participants.count(), 3)

# TODO: integration test
# class PromotionViewTests(TestCase):

