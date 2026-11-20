from rest_framework import generics

from .models import Listing
from .serializers import ListingSerializer


class ListingListView(generics.ListAPIView):
    """Read-only list of listings, to check the models and serializers. Full CRUD comes in 0x01."""
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer
