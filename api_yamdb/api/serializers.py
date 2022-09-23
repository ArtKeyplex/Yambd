from django.db.models import Avg

from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from reviews.models import Comment, Reviews


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('reviews',)


class ReviewsSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(
        slug_field='username',
        read_only=True
    )
    rating = serializers.SerializerMethodField()

    def get_rating(self, ob):
        return ob.reviews.all().aggregate(Avg('score'))

    class Meta:
        fields = '__all__'
        model = Reviews
