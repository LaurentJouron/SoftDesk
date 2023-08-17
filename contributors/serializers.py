from rest_framework import serializers

from users.models import User
from .models import Contributor


class ContributorSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        queryset=User.objects.all(), slug_field='username'
    )
    project = serializers.SlugRelatedField(read_only=True, slug_field='id')

    class Meta:
        model = Contributor
        fields = ['id', 'permission', 'role', 'user', 'project']
