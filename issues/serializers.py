from rest_framework import serializers
from django.db.models import Q
from django.contrib.auth import get_user_model

from .models import Issue, TagChoice, PriorityChoice, StatusChoice

User = get_user_model()


class IssueSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.ReadOnlyField(source="author.username")
    assignee = serializers.SlugRelatedField(
        many=False,
        read_only=False,
        slug_field="username",
        queryset=User.objects.all(),
    )
    comments = serializers.HyperlinkedRelatedField(
        many=True, read_only=True, view_name="comment-detail"
    )
    tag = serializers.SlugRelatedField(
        many=False, slug_field="name", queryset=TagChoice.objects.all()
    )
    priority = serializers.SlugRelatedField(
        many=False, slug_field="name", queryset=PriorityChoice.objects.all()
    )
    status = serializers.SlugRelatedField(
        many=False, slug_field="name", queryset=StatusChoice.objects.all()
    )
    project = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Issue
        fields = [
            "id",
            "url",
            "title",
            "description",
            "tag",
            "priority",
            "status",
            "created",
            "modified",
            "is_active",
            "author",
            "assignee",
            "project",
            "comments",
        ]

    def __str__(self):
        return self.title

    def __init__(self, *args, **kwargs):
        project_pk = self.context.get("project_pk") 
        super().__init__(*args, **kwargs)
        self.fields["assignee"].queryset = User.objects.filter(Q(contributed_projects__pk=project_pk) | Q(projects__pk=project_pk), is_active=True),
