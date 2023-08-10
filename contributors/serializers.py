from rest_framework import serializers

from .models import Contributor


class ContributorSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    project = serializers.ReadOnlyField(source='project.title')

    class Meta:
        model = Contributor
        fields = ['user', 'project', 'permission']
