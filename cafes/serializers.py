from django.db import transaction
from rest_framework import serializers

from .models import Barrio, Cafe, Dish, Review, Reviewer, Tag


class ReviewerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviewer
        fields = ["name", "join_date"]


class ReviewSerializer(serializers.ModelSerializer):
    cafe_name = serializers.ReadOnlyField(source="cafe.name")
    reviewer_name = serializers.ReadOnlyField(source="reviewer.name")

    class Meta:
        model = Review
        fields = ["id", "cafe_name", "reviewer", "reviewer_name", "comment", "rating"]


class DishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dish
        fields = ["name", "price", "is_vegan"]


class BarrioSerializer(serializers.ModelSerializer):

    class Meta:
        model = Barrio
        fields = ["name", "id", "comuna"]


class CafeSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, required=False)
    dishes = DishSerializer(many=True, required=False)
    barrio = BarrioSerializer(read_only=True)
    barrio_name = serializers.SlugRelatedField(
        queryset=Barrio.objects.all(),
        slug_field="name",
        source="barrio",
        write_only=True,
    )
    tag_names = serializers.SlugRelatedField(
        many=True,
        queryset=Tag.objects.all(),
        slug_field="name",
        source="tag",
        write_only=True,
        required=False,
    )

    class Meta:
        model = Cafe
        fields = [
            "id",
            "name",
            "barrio",
            "address",
            "has_good_medialunas",
            "notes",
            "recommendation_count",
            "tag",
            "reviews",
            "review_count",
            "tagline",
            "dishes",
            "barrio_name",
            "tag_names",
        ]

    tagline = serializers.SerializerMethodField()

    def get_tagline(self, obj):
        if obj.review_count > 5:
            tagline = "Local favourite!"
        elif obj.review_count <= 5 and obj.review_count > 0:
            tagline = "Hidden gem!"
        elif obj.review_count == 0:
            tagline = "Be the first to visit!"
        return tagline

    tag = serializers.SlugRelatedField(many=True, read_only=True, slug_field="name")

    @transaction.atomic
    def create(self, validated_data):
        reviews_data = validated_data.pop("reviews", [])
        dish_data = validated_data.pop("dishes", [])
        tag_data = validated_data.pop("tag", [])
        cafe = Cafe.objects.create(**validated_data)

        if tag_data:
            cafe.tag.set(tag_data)

        for review_data in reviews_data:
            Review.objects.create(cafe=cafe, **review_data)

        for data in dish_data:
            Dish.objects.create(cafe=cafe, **data)
        return cafe

    def get_barrio(self, obj):
        return obj.barrio.label

    def get_summary(self, obj):
        return f"{obj.name} is a {obj.rating}-star cafe."
