from rest_framework import serializers
from pygments import highlight
from pygments.formatters.html import HtmlFormatter
from pygments.lexers import get_lexer_by_name

from .models import Project


class ProjectSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(
        view_name='project-highlight', format='html'
    )

    class Meta:
        model = Project
        fields = [
            'url',
            'id',
            'highlight',
            'is_active',
            'created',
            'title',
            'description',
            'type_choice',
            'owner',
        ]

    def create(self, validated_data):
        return Project.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.created = validated_data.get('created', instance.created)
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get(
            'description', instance.description
        )
        instance.type_choice = validated_data.get(
            'type_choice', instance.type_choice
        )
        instance.is_active = validated_data.get(
            'is_active', instance.is_active
        )
        instance.owner = validated_data.get('owner', instance.owner)
        instance.save()
        return instance

    def save(self, *args, **kwargs):
        instance = super().save(*args, **kwargs)
        type_choice = instance.type_choice
        is_active = 'table' if instance.is_active else False
        options = {'title': instance.title} if instance.title else {}
        formatter = HtmlFormatter(
            style=self.style, is_active=is_active, full=True, **options
        )
        lexer = get_lexer_by_name(type_choice)
        self.highlighted = highlight(instance.created, lexer, formatter)
        super().save(*args, **kwargs)
