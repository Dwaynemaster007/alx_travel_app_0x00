from datetime import date, timedelta
from decimal import Decimal

from django.contrib.auth import get_user_model
from django.core.management import call_command
from django.test import TestCase
from io import StringIO

from .models import Booking, Listing, Review


class ModelTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user('guest', 'guest@example.com', 'Str0ng-pass!')
        self.listing = Listing.objects.create(title='Cabin', description='Quiet', location='Kigali', price_per_night=Decimal('80'))

    def test_booking_total_price(self):
        booking = Booking.objects.create(listing=self.listing, user=self.user, check_in=date(2026, 1, 1), check_out=date(2026, 1, 4))
        self.assertEqual(booking.nights, 3)
        self.assertEqual(booking.total_price, Decimal('240.00'))

    def test_review(self):
        review = Review.objects.create(listing=self.listing, user=self.user, rating=5)
        self.assertIn('Cabin', str(review))

    def test_seed_command(self):
        call_command('seed', '--listings', '3', stdout=StringIO())
        self.assertEqual(Listing.objects.count(), 4)
        self.assertEqual(Booking.objects.count(), 3)

    def test_swagger_docs(self):
        self.assertEqual(self.client.get('/swagger/?format=openapi').status_code, 200)
