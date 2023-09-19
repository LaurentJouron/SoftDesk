from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import Project, TypeChoice

User = get_user_model()


class TypeChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeChoice
        fields = ("id", "name")


class ProjectSerializer(serializers.HyperlinkedModelSerializer):

    author = serializers.ReadOnlyField(source="author.username")
    contributor = serializers.SlugRelatedField(
        many=True,
        queryset=User.objects.all(),
        slug_field="username",
    )
    type_choice = serializers.SlugRelatedField(
        queryset=TypeChoice.objects.all(), many=False, slug_field="name"
    )
    issues = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name="issue-detail")

    class Meta:
        model = Project
        fields = [
            "id",
            "url",
            "author",
            "title",
            "description",
            "type_choice",
            "contributor",
            "created",
            "modified",
            "issues",
        ]

    def __str__(self):
        return self.title
