from rest_framework import serializers
from contributors.serializers import ContributorSerializer

from users.models import User
from comments.serializers import CommentSerializer
from .models import Issue


class IssueSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    assignee = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    contributors = ContributorSerializer(many=True, read_only=True)
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Issue
        fields = [
            'id',
            'url',
            'title',
            'description',
            'tag_choices',
            'priority_choices',
            'status_choices',
            'created',
            'modified',
            'is_active',
            'author',
            'assignee',
            'project',
            'contributors',
            'comments',
        ]

    def __str__(self):
        return self.title

    def create(self, validated_data):
        assignee_data = validated_data.pop('assignee', None)
        issue = Issue.objects.create(**validated_data)
        if assignee_data:
            issue.assignee = assignee_data
            issue.save()
        return issue

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get(
            'description', instance.description
        )
        instance.tag_choices = validated_data.get(
            'tag_choices', instance.tag_choices
        )
        instance.priority_choices = validated_data.get(
            'priority_choices', instance.priority_choices
        )
        instance.status_choices = validated_data.get(
            'status_choices', instance.status_choices
        )
        instance.created = validated_data.get('created', instance.created)
        instance.modified = validated_data.get('modified', instance.modified)
        instance.is_active = validated_data.get(
            'is_active', instance.is_active
        )
        instance.assignee = validated_data.get('assignee', instance.assignee)
        instance.author = validated_data.get('author', instance.author)
        instance.project = validated_data.get('project')
        instance.save()
        return instance
