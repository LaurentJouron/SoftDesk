from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    projects = serializers.HyperlinkedRelatedField(
        many=True, view_name='comment-detail', read_only=True
    )

    class Meta:
        model = User
        fields = [
            'id',
            'url',
            'username',
            'first_name',
            'last_name',
            'email',
            'password',
            'is_superuser',
            'is_staff',
            'is_active',
            'projects',
        ]

    def get_projects(self, obj):
        return [project.name for project in obj.projects.all()]

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email'],
            password=validated_data['password'],
            is_superuser=validated_data['is_superuser'],
            is_staff=validated_data['is_staff'],
            is_active=validated_data['is_active'],
        )
        return user
