from rest_framework import serializers

from users.models import User, ProjectContributor
from .models import Project


class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    issues = serializers.HyperlinkedRelatedField(
        many=True, read_only=True, view_name='issue-detail'
    )
    contributors = serializers.HyperlinkedRelatedField(
        many=True, read_only=True, view_name='contributor-detail'
    )
    assignee = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Project
        fields = [
            'url',
            'id',
            'author',
            'title',
            'description',
            'type_choices',
            'assignee',
            'created',
            'modified',
            'is_active',
            'issues',
            'contributors',
        ]

    def __str__(self):
        return self.title

    def create(self, validated_data):
        return Project.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get(
            'description', instance.description
        )
        instance.type_choices = validated_data.get(
            'type_choices', instance.type_choices
        )
        instance.assignee = validated_data.get('assignee', instance.assignee)
        instance.created = validated_data.get('created', instance.created)
        instance.modified = validated_data.get('modified', instance.modified)
        instance.author = validated_data.get('author', instance.author)
        instance.is_active = validated_data.get(
            'is_active', instance.is_active
        )
        instance.save()
        return instance
