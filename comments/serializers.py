from rest_framework import serializers
from pygments import highlight
from pygments.formatters.html import HtmlFormatter
from pygments.lexers import get_lexer_by_name

from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(
        view_name='comment-highlight', format='html'
    )

    class Meta:
        model = Comment
        fields = [
            'url',
            'id',
            'highlight',
            'description',
            'author_user',
            'issue',
            'created_datetime',
            'owner',
        ]

    def create(self, validated_data):
        return Comment.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.created_datetime = validated_data.get(
            'created_datetime', instance.created_datetime
        )
        instance.description = validated_data.get(
            'description', instance.description
        )
        instance.author_user = validated_data.get(
            'author_user', instance.author_user
        )
        instance.issue = validated_data.get('issue', instance.issue)
        instance.created_datetime = validated_data.get(
            'created_datetime', instance.created_datetime
        )
        instance.owner = validated_data.get('owner', instance.owner)
        instance.save()
        return instance

    def save(self, *args, **kwargs):
        instance = super().save(*args, **kwargs)
        description = instance.description
        author_user = 'table' if instance.author_user else False
        options = {'issue': instance.issue} if instance.issue else {}
        formatter = HtmlFormatter(
            style=self.style, description=description, full=True, **options
        )
        lexer = get_lexer_by_name(author_user)
        self.highlighted = highlight(instance.created, lexer, formatter)
        super().save(*args, **kwargs)
