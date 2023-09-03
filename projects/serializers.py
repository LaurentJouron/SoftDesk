from re import T
from rest_framework import serializers
from django.contrib.auth import get_user_model

from .models import Project, TypeChoice

User = get_user_model()


class TypeChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeChoice
        fields = ('id', 'name')


class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    contributor = serializers.SlugRelatedField(
        many=True,
        queryset=User.objects.all(),
        slug_field='username',
    )
    type_choice = serializers.SlugRelatedField(
        queryset=TypeChoice.objects.all(), many=False, slug_field='name'
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
