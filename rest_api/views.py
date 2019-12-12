from rest_framework import generics

from locations.models import Page
from rest_api.serializer import PageSerializer

class PageList(generics.ListCreateAPIView):
    queryset = Page.objects.all()
    serializer_class = PageSerializer

class PageDetail(generics.RetrieveDestroyAPIView):
    queryset = Page.objects.all()
    serializer_class = PageSerializer
