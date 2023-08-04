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
            'projects',
        ]

    def get_projects(self, obj):
        return [project.name for project in obj.projects.all()]


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email'],
            password=validated_data['password'],
        )
        return user
