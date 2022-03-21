from django.utils import timezone
from django.core.validators import MaxValueValidator
from rest_framework import serializers

from reviews import models


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        exclude = ('id',)


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Genre
        exclude = ('id',)


class TitleSerializer(serializers.ModelSerializer):
    genre = GenreSerializer(many=True)
    category = CategorySerializer()
    rating = serializers.IntegerField(required=False)

    class Meta:
        read_only_field = ('__all__',)
        model = models.Title
        fields = ('id', 'name', 'year', 'rating', 'description', 'genre',
                  'category')



class TitlePostSerializer(serializers.ModelSerializer):
    genre = serializers.SlugRelatedField(
        many=True,
        slug_field='slug',
        queryset=models.Genre.objects.all()
    )
    categpry = serializers.SlugRelatedField(
        slug_field='slug',
        queryset=models.Category.objects.all()
    )
    year = serializers.IntegerField(
        validators=(MaxValueValidator(
            timezone.now().year,
            message='Год не может быть больше текущего!'
        ),)
    )

    class Meta:
        model = models.Title
        fields = ('id', 'name', 'year', 'description', 'genre', 'category')
