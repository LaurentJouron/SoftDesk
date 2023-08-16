from .models import Project
from .relations import ProjectSerializer, ProjectRelatedSerializer


class ProjectSerializer(ProjectSerializer):
    class Meta(ProjectSerializer.Meta):
        model = Project
        fields = [
            'url',
            'id',
            'author',
            'title',
            'description',
            'type_choices',
            'is_active',
            'created',
            'modified',
            'issues',
            'contributors',
        ]

    def get_contributors(self, obj):
        contributors = obj.contributors_set.all()
        return ProjectRelatedSerializer(contributors, many=True).data

    def __str__(self):
        return self.title

    def create(self, validated_data):
        return Project.objects.create(**validated_data)
