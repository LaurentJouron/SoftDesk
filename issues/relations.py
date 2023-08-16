from rest_framework import serializers
from .models import Issue


class IssueSerializer(serializers.HyperlinkedModelSerializer):
    issues = serializers.SerializerMethodField()

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
            'comments',
        ]

    def get_issues(self, obj):
        issues = Issue.objects.filter(project=obj)
        issue_serializer = IssueRelatedSerializer(
            issues, many=True, context=self.context
        )
        return issue_serializer.data


class IssueRelatedSerializer(serializers.Serializer):
    ...
