from rest_framework import serializers

from users.models import User
from .models import Project, TypeChoice


class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    issues = serializers.HyperlinkedRelatedField(
        many=True, read_only=True, view_name='issue-detail'
    )
    contributor = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), many=True
    )
    type_choice = serializers.PrimaryKeyRelatedField(
        queryset=TypeChoice.objects.all(), many=False
    )

    class Meta:
        model = Project
        fields = [
            'url',
            'id',
            'author',
            'title',
            'description',
            'type_choice',
            'contributor',
            'created',
            'modified',
            'is_active',
            'issues',
        ]

    def __str__(self):
        return self.title

    def create(self, validated_data):
        contributors_data = validated_data.pop('contributor', [])
        project = Project.objects.create(**validated_data)
        project.contributor.set(contributors_data)
        return project

    def update(self, instance, validated_data):
        contributors_data = validated_data.pop('contributor', [])
        instance = super().update(instance, validated_data)
        instance.contributor.set(contributors_data)
        return instance
