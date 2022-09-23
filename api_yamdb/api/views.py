from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination

from ..reviews import User
from api.permissions import IsAuthorOrReadOnly
from api.serializers import (
    CommentSerializer,
    ReviewsSerializer
)
from reviews.models import Reviews, Title


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()


class ReviewsViewSet(viewsets.ModelViewSet):
    queryset = Reviews.objects.all()
    serializer_class = ReviewsSerializer
    permission_classes = [IsAuthorOrReadOnly, ]
    pagination_class = PageNumberPagination

    def get_title(self):
        return get_object_or_404(
            Title,
            id=self.kwargs['title_id']
        )

    def get_queryset(self):
        return self.get_title().reviews.all()

    def perform_create(self, serializer):
        serializer.save(
            author=self.request.user,
            title=self.get_title()
        )


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthorOrReadOnly, ]
    pagination_class = PageNumberPagination

    def get_review(self):
        return get_object_or_404(
            Reviews,
            id=self.kwargs['review_id']
        )

    def get_queryset(self):
        return self.get_review().comments.all()

    def perform_create(self, serializer):
        serializer.save(
            author=self.request.user,
            review=self.get_review()
        )
