from rest_framework import serializers
from contributors.serializers import ContributorSerializer
from .models import Project


class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = [
            'url',
            'id',
            'author',
            'title',
            'description',
            'type_choices',
            'is_active',
            'created',
            'modified',
            'issues',
            'contributors',
        ]


class ProjectRelatedSerializer(serializers.Serializer):
    contributors = ContributorSerializer(many=True, read_only=True)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get(
            'description', instance.description
        )
        instance.type_choices = validated_data.get(
            'type_choices', instance.type_choices
        )
        instance.is_active = validated_data.get(
            'is_active', instance.is_active
        )
        instance.created = validated_data.get('created', instance.created)
        instance.modified = validated_data.get('modified', instance.modified)
        instance.author = validated_data.get('author', instance.author)
        instance.save()
        return instance
