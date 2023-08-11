from rest_framework import serializers
from rest_framework import status
from rest_framework.response import Response

from django.contrib.auth.models import User
from .models import Comment


from rest_framework import serializers
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
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

    # def create(self, validated_data):
    #     request = self.context.get('request')
    #     author_id = request.user.id
    #     validated_data['author'] = User.objects.get(id=author_id)
    #     comment = Comment.objects.create(**validated_data)
    #     return comment
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
