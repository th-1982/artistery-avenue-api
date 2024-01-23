from django.db.models import Count, Avg
from rest_framework import generics, permissions, filters
from drf_api.permissions import IsOwnerOrReadOnly
from .models import Artist
from .serializers import ArtistSerializer


class ArtistList(generics.ListCreateAPIView):
    """
    List comments or create a comment if logged in.
    """
    serializer_class = ArtistSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    # Calculate the total number of reviews and an average rating
    # related to each artist.
    queryset = Artist.objects.annotate(
        reviews_count=Count('reviews', distinct=True),
        average_rating=Avg('reviews__rating')
    ).order_by('-created_at')

    filter_backends = [
        filters.SearchFilter
    ]

    search_fields = [
        'owner__username',
        'speciality',
        'location'
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ArtistDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a comment, or update or delete it by id if you own it.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = ArtistSerializer
    queryset = Artist.objects.annotate(
        reviews_count=Count('reviews', distinct=True),
        average_rating=Avg('reviews__rating')
    ).order_by('-created_at')
