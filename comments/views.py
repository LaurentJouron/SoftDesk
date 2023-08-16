from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import renderers

from .models import Comment
from .serializers import CommentRelatedSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    permission_classes = []
    serializer_class = CommentRelatedSerializer

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        comment = self.get_object()
        return Response(comment.highlighted)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
