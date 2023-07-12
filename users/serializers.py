from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework import serializers
from pygments import highlight
from pygments.formatters.html import HtmlFormatter
from pygments.lexers import get_lexer_by_name


class UserSerializer(serializers.ModelSerializer):
    projects = serializers.HyperlinkedRelatedField(
        many=True, view_name='project-detail', read_only=True
    )
    password = serializers.CharField(
        write_only=True, required=True, style={'input_type': 'password'}
    )

    class Meta:
        model = User
        fields = [
            'url',
            'id',
            'username',
            'first_name',
            'last_name',
            'email',
            'password',
            'projects',
            'is_active',
            'is_superuser',
            'is_staff',
            'date_joined',
        ]
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.first_name = validated_data.get(
            'first_name', instance.first_name
        )
        instance.last_name = validated_data.get(
            'last_name', instance.last_name
        )
        instance.email = validated_data.get('email', instance.email)
        instance.password = validated_data.get('password', instance.password)
        instance.projects = validated_data.get('projects', instance.projects)
        instance.is_active = validated_data.get(
            'is_active', instance.is_active
        )
        instance.is_superuser = validated_data.get(
            'is_superuser', instance.is_superuser
        )
        instance.is_staff = validated_data.get('is_staff', instance.is_staff)
        instance.date_joined = validated_data.get(
            'date_joined', instance.date_joined
        )
        instance.save()
        return instance

    def save(self, *args, **kwargs):
        instance = super().save(*args, **kwargs)
        is_active = 'table' if instance.is_active else False
        options = {'username': instance.username} if instance.username else {}
        formatter = HtmlFormatter(
            style=self.style, is_active=is_active, full=True, **options
        )
        lexer = get_lexer_by_name('first_name')
        self.highlighted = highlight(instance.created, lexer, formatter)
        super().save(*args, **kwargs)