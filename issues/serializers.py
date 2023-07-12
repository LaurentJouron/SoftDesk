from rest_framework import serializers
from pygments import highlight
from pygments.formatters.html import HtmlFormatter
from pygments.lexers import get_lexer_by_name

from .models import Issue


class IssueSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(
        view_name='issue-highlight', format='html'
    )

    class Meta:
        model = Issue
        fields = [
            'url',
            'id',
            'highlight',
            'title',
            'description',
            'tag_choices',
            'priority_choices',
            'status_choices',
            'created_time',
            'owner',
        ]

    def create(self, validated_data):
        return Issue.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get(
            'description', instance.description
        )
        instance.tag_choices = validated_data.get(
            'tag_choices', instance.tag_choices
        )
        instance.priority_choices = validated_data.get(
            'priority_choices', instance.priority_choices
        )
        instance.status_choices = validated_data.get(
            'status_choices', instance.status_choices
        )
        instance.created_time = validated_data.get(
            'created_time', instance.created_time
        )
        instance.owner = validated_data.get('owner', instance.owner)
        instance.save()
        return instance

    def save(self, *args, **kwargs):
        instance = super().save(*args, **kwargs)
        tag_choices = instance.tag_choices
        priority_choices = 'table' if instance.priority_choices else False
        options = {'title': instance.title} if instance.title else {}
        formatter = HtmlFormatter(
            style=self.style,
            priority_choices=priority_choices,
            full=True,
            **options,
        )
        lexer = get_lexer_by_name(tag_choices)
        self.highlighted = highlight(instance.created, lexer, formatter)
        super().save(*args, **kwargs)
