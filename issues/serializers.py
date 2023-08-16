from .relations import Issue, IssueSerializer


class IssueSerializer(IssueSerializer):
    class Meta(IssueSerializer.Meta):
        model = Issue

    def create(self, validated_data):
        assignee_data = validated_data.pop('assignee', None)
        issue = Issue.objects.create(**validated_data)
        if assignee_data:
            issue.assignee = assignee_data
            issue.save()
        return issue

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
        instance.created = validated_data.get('created', instance.created)
        instance.modified = validated_data.get('modified', instance.modified)
        instance.is_active = validated_data.get(
            'is_active', instance.is_active
        )
        instance.assignee = validated_data.get('assignee', instance.assignee)
        instance.author = validated_data.get('author', instance.author)
        instance.project = validated_data.get('project')
        instance.save()
        return instance
