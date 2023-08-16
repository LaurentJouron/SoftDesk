from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from projects.models import Project
from projects.serializers import ProjectSerializer


class UserSerializer(serializers.HyperlinkedModelSerializer):
    # Serializer for the User model

    # HyperlinkedRelatedField for projects_contributed relationship
    projects = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='project-detail',
        source='projects_contributed',
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
        # Retrieve projects associated with the user through contributors
        contributors = obj.contributors_set.all()
        project_ids = [contributor.project.id for contributor in contributors]
        projects = Project.objects.filter(id__in=project_ids)
        return ProjectSerializer(projects, many=True).data

    def create(self, validated_data):
        # Create a new user
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

    def update(self, instance, validated_data):
        # Update user details
        if 'password' in validated_data:
            validated_data['password'] = make_password(
                validated_data['password']
            )
        return super().update(instance, validated_data)


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    # Custom TokenObtainPairSerializer to include 'username' in token payload

    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)
        token['username'] = user.username
        return token
