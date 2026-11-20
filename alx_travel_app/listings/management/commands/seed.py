import random
from datetime import date, timedelta
from decimal import Decimal

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

from listings.models import Booking, Listing, Review

TITLES = ['Beachside Bungalow', 'Mountain Retreat', 'Downtown Apartment', 'Cozy Cabin', 'Luxury Villa']
LOCATIONS = ['Mombasa', 'Nairobi', 'Kigali', 'Cape Town', 'Accra', 'Mbabane']


class Command(BaseCommand):
    help = 'Seed the database with sample listings, bookings and reviews'

    def add_arguments(self, parser):
        parser.add_argument('--listings', type=int, default=10, help='How many listings to create')

    def handle(self, *args, **options):
        User = get_user_model()
        host, _ = User.objects.get_or_create(username='sample_host', defaults={'email': 'host@example.com'})
        guest, _ = User.objects.get_or_create(username='sample_guest', defaults={'email': 'guest@example.com'})

        for i in range(options['listings']):
            listing = Listing.objects.create(
                host=host,
                title=f'{random.choice(TITLES)} #{Listing.objects.count() + 1}',
                description='A wonderful place to stay!',
                location=random.choice(LOCATIONS),
                price_per_night=Decimal(random.randint(50, 300)),
            )
            start = date.today() + timedelta(days=random.randint(1, 60))
            Booking.objects.create(listing=listing, user=guest, check_in=start, check_out=start + timedelta(days=random.randint(1, 7)))
            Review.objects.create(listing=listing, user=guest, rating=random.randint(3, 5), comment='Lovely stay.')
            self.stdout.write(self.style.SUCCESS(f'Created: {listing}'))

        self.stdout.write(self.style.SUCCESS(f"Done. {Listing.objects.count()} listings in the database."))
