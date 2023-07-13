from rest_framework.serializers import ModelSerializer

from .models import Contributor


class ContributorSerializer(ModelSerializer):
    """
    Serializer for the Contributor model.

    Fields:
        user (ForeignKey): The user associated with the contributor.

    Meta:
        model (Contributor): The model class associated with the serializer.
        fields (list[str]): The fields to include in the serialized representation.
    """

    class Meta:
        model = Contributor
        fields = [
            'user',
        ]
