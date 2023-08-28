from rest_framework import serializers

from .models import Issue, TagChoice, PriorityChoice, StatusChoice


class IssueSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    assignee = serializers.SlugRelatedField(
        many=False, read_only=True, slug_field='username'
    )
    comments = serializers.HyperlinkedRelatedField(
        many=True, read_only=True, view_name='comment-detail'
    )
    tag = serializers.SlugRelatedField(
        slug_field='name', queryset=TagChoice.objects.all()
    )
    priority = serializers.SlugRelatedField(
        slug_field='name', queryset=PriorityChoice.objects.all()
    )
    status = serializers.SlugRelatedField(
        slug_field='name', queryset=StatusChoice.objects.all()
    )

    class Meta:
        model = Issue
        fields = [
            'id',
            'url',
            'title',
            'description',
            'tag',
            'priority',
            'status',
            'created',
            'modified',
            'is_active',
            'author',
            'assignee',
            'project',
            'comments',
        ]

    def __str__(self):
        return self.title

    def create(self, validated_data):
        return Issue.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get(
            'description', instance.description
        )
        instance.tag = validated_data.get('tag', instance.tag)
        instance.priority = validated_data.get('priority', instance.priority)
        instance.status = validated_data.get('status', instance.status)
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
