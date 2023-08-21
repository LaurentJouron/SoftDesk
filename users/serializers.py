from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from projects.models import Project
from projects.serializers import ProjectSerializer
from .models import User, ProjectContributor


class UserSerializer(serializers.HyperlinkedModelSerializer):
    projects = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='project-detail',
        source='projects_contributed',
    )
    contributors = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='project-detail',
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
            'contributors',
        ]

    def get_projects(self, obj):
        contributors = obj.contributors_set.all()
        project_ids = [contributor.project.id for contributor in contributors]
        projects = Project.objects.filter(id__in=project_ids)
        return ProjectSerializer(projects, many=True).data

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email'],
            password=validated_data['password'],
        )
        return user

    def update(self, instance, validated_data):
        if 'password' in validated_data:
            validated_data['password'] = make_password(
                validated_data['password']
            )
        return super().update(instance, validated_data)


class ContributorSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        queryset=User.objects.all(), slug_field='username'
    )
    project = serializers.SlugRelatedField(read_only=True, slug_field='id')

    class Meta:
        model = ProjectContributor
        fields = ['id', 'permission', 'user', 'project']

    def create(self, validated_data):
        return ProjectContributor.objects.create(**validated_data)
