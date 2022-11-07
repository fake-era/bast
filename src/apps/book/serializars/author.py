from rest_framework import serializers

from apps.book.models import Author


class AuthorRetrieveOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"
