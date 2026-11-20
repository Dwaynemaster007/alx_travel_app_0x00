from rest_framework import serializers

from .models import Booking, Listing, Review


class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Review
        fields = ['id', 'listing', 'user', 'rating', 'comment', 'created_at']
        read_only_fields = ['user', 'created_at']


class ListingSerializer(serializers.ModelSerializer):
    host = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Listing
        fields = ['id', 'title', 'description', 'location', 'price_per_night', 'host', 'created_at']
        read_only_fields = ['host', 'created_at']


class BookingSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Booking
        fields = ['id', 'listing', 'user', 'check_in', 'check_out', 'total_price', 'status', 'created_at']
        read_only_fields = ['user', 'total_price', 'status', 'created_at']

    def validate(self, attrs):
        check_in = attrs.get('check_in', getattr(self.instance, 'check_in', None))
        check_out = attrs.get('check_out', getattr(self.instance, 'check_out', None))
        if check_in and check_out and check_out <= check_in:
            raise serializers.ValidationError({'check_out': 'Check-out must be after check-in.'})
        return attrs
