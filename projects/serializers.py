from re import T
from rest_framework import serializers

from users.models import User
from .models import Project, TypeChoice


class TypeChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeChoice
        fields = ('id', 'name')


class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    issues = serializers.HyperlinkedRelatedField(
        many=True, read_only=True, view_name='issue-detail'
    )
    contributor = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), many=False
    )
    # type_choice = serializers.PrimaryKeyRelatedField(
    #     queryset=TypeChoice.objects.all()
    # )
    type_choice = TypeChoiceSerializer(many=False)

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
        type_choices_data = validated_data.pop('type_choice')
        contributors_data = validated_data.pop('contributor', [])
        project = Project.objects.create(**validated_data)
        project.contributor.set(contributors_data)
        for type_choice_data in type_choices_data:
            TypeChoice.objects.create(project=project, **type_choice_data)
        return project

    def update(self, instance, validated_data):
        contributors_data = validated_data.pop('contributor', [])
        type_choice = validated_data.pop('type_choice', None)
        if type_choice:
            type_choice = TypeChoice.objects.get(name=type_choice)
            instance.type_choice = type_choice
        instance = super().update(instance, validated_data)
        instance.contributor.set(contributors_data)
        return instance
