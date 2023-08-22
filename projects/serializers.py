from rest_framework import serializers

from users.models import User
from .models import Project


class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    issues = serializers.HyperlinkedRelatedField(
        many=True, read_only=True, view_name='issue-detail'
    )
    assignees = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), many=True
    )

    class Meta:
        model = Project
        fields = [
            'url',
            'id',
            'author',
            'title',
            'description',
            'type_choices',
            'assignees',
            'created',
            'modified',
            'is_active',
            'issues',
        ]

    def __str__(self):
        return self.title

    def create(self, validated_data):
        assignees_data = validated_data.pop('assignees', [])
        project = Project.objects.create(**validated_data)
        project.assignees.set(assignees_data)
        return project

    def update(self, instance, validated_data):
        assignees_data = validated_data.pop('assignees', [])
        instance = super().update(instance, validated_data)
        instance.assignees.set(assignees_data)
        return instance
