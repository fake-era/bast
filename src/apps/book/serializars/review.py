from rest_framework import serializers

from apps.book.models import Review


class ReviewRetrieveOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"


class ReviewCreateInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"
