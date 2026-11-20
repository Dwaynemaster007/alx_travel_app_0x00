from django.contrib import admin

from .models import Booking, Listing, Review


@admin.register(Listing)
class ListingAdmin(admin.ModelAdmin):
    list_display = ('title', 'location', 'price_per_night', 'host', 'created_at')
    search_fields = ('title', 'location')


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('listing', 'user', 'check_in', 'check_out', 'total_price', 'status')
    list_filter = ('status',)


admin.site.register(Review)
