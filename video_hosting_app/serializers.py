from django.db import transaction
from rest_framework import serializers

from video_hosting_app.models import *


class GenresSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentGenre
        fields = ["name"]


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentCategory
        fields = ["name"]


class StatisticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentStatistics
        fields = ["number_of_views", "number_of_likes", "number_of_dislikes"]


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = "__all__"


class PreviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Preview
        fields = "__all__"


class MainContentPostSerializer(serializers.ModelSerializer):
    genres = GenresSerializer(many=True, required=False)
    category = CategorySerializer(many=True, required=False)
    statistics = StatisticsSerializer(required=False)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if representation.get("video"):
            representation["video"] = VideoSerializer(Video.objects.get(id=representation["video"])).data["video"]
        if representation.get("preview"):
            representation["preview"] = PreviewSerializer(Preview.objects.get(id=representation["preview"])).data[
                "preview"
            ]
        return representation

    class Meta:
        model = ContentPost
        fields = ["id", "title", "description", "genres", "video", "preview", "url", "category", "statistics"]


class CreateContentPostSerializer(MainContentPostSerializer):
    genres = serializers.ListField(write_only=True)
    category = serializers.ListField(write_only=True)

    def create(self, validated_data):
        with transaction.atomic():
            genres = validated_data.pop("genres", None)
            categories = validated_data.pop("category", None)
            statistics = validated_data.pop("statistics", None)

            post_statistics = ContentStatistics.objects.create(**statistics)
            post = ContentPost.objects.create(statistics=post_statistics, **validated_data)

            for genre in genres:
                content_genre, _ = ContentGenre.objects.get_or_create(name=genre["name"])
                post.genres.add(content_genre)

            for category in categories:
                content_category, _ = ContentCategory.objects.get_or_create(name=category["name"])
                post.category.add(content_category)

            post.save()
            return post


class PlaylistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playlist
        fields = ["title", "content_posts", "channel", "number_of_posts"]
        extra_kwargs = {"channel": {"write_only": True}, "content_posts": {"write_only": True}}


class ChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Channel
        fields = "__all__"
