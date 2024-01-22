from rest_framework import generics
from artistery_avenue.permissions import IsOwnerOrReadOnly
from .models import Artist
from .serializers import ArtistSerializer


class ArtistList(generics.ListCreateAPIView):
    """
    List comments or create a comment if logged in.
    """
    serializer_class = ArtistSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Artist.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ArtistDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a comment, or update or delete it by id if you own it.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = ArtistSerializer
    queryset = Artist.objects.all()