from rest_framework import serializers
from .models import Contributor
from projects.serializers import ProjectSerializer


class ContributorProjectSerializer(serializers.ModelSerializer):
    project = ProjectSerializer()

    class Meta:
        model = Contributor
        fields = ['project', 'permission', 'role']
