from rest_framework import serializers

from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    issue = serializers.HyperlinkedRelatedField(
        many=True, read_only=True, view_name='issue-detail'
    )

    class Meta:
        model = Comment
        fields = [
            'id',
            'url',
            'description',
            'issue',
            'author',
            'created',
            'modified',
        ]

    def __str__(self):
        return self.title

    def create(self, validated_data):
        user = self.context['request'].user
        data = {**validated_data, 'author': user}
        comment = Comment.objects.create(**data)
        return comment

    def update(self, instance, validated_data):
        instance.description = validated_data.get(
            'description', instance.description
        )
        instance.issue = validated_data.get('issue', instance.issue)
        instance.author = validated_data.pop('author')
        instance.created = validated_data.get('created', instance.created)
        instance.modified = validated_data.get('modified', instance.modified)
        instance.save()
        return instance
