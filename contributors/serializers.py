from rest_framework import serializers

from .models import Contributor


class ContributorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contributor
        fields = ['user', 'project', 'permission']
