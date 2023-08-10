from rest_framework import serializers

from users.models import User
from .models import Comment


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    # author = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    author = serializers.ReadOnlyField(source='author.username')

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
        comment = Comment.objects.create(**validated_data)
        return comment

    def update(self, instance, validated_data):
        instance.description = validated_data.get(
            'description', instance.description
        )
        instance.issue = validated_data.get('issue', instance.issue)
        instance.author = validated_data.get('author', instance.author)
        instance.created = validated_data.get('created', instance.created)
        instance.modified = validated_data.get('modified', instance.modified)
        instance.save()
        return instance
