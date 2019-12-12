from rest_framework import serializers

from locations.models import Page

class PageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Page
        fields = "__all__"