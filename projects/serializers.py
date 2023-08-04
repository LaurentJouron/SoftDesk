from rest_framework import serializers
from contributors.serializers import ContributorSerializer
from .models import Project


class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.CurrentUserDefault()
    issues = serializers.HyperlinkedRelatedField(
        many=True, read_only=True, view_name='issue-detail'
    )
    contributors = serializers.HyperlinkedRelatedField(
        many=True, read_only=True, view_name='contributor-detail'
    )

    class Meta:
        model = Project
        fields = [
            'url',
            'id',
            'owner',
            'title',
            'description',
            'type_choices',
            'is_active',
            'created',
            'modified',
            'issues',
            'contributors',
        ]

    def get_contributors(self, obj):
        contributors = obj.contributors_set.all()
        return ContributorSerializer(contributors, many=True).data

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
        instance.is_active = validated_data.get(
            'is_active', instance.is_active
        )
        instance.created = validated_data.get('created', instance.created)
        instance.modified = validated_data.get('modified', instance.modified)
        instance.owner = validated_data.get('owner', instance.owner)
        instance.save()
        return instance
