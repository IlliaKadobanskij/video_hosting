from django.db import models

from video_hosting_app.storage_backends import *


class Video(models.Model):
    video = models.FileField("Video", storage=VideoStorage)

    def __str__(self):
        return f"{self.video}"

    class Meta:
        verbose_name = "Video"
        verbose_name_plural = "Videos"


class Preview(models.Model):
    preview = models.ImageField("Poster", storage=PreviewStorage)

    def __str__(self):
        return f"{self.preview}"

    class Meta:
        verbose_name = "Preview"
        verbose_name_plural = "Previews"


class ContentGenre(models.Model):
    name = models.CharField("Genre", max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Genre"
        verbose_name_plural = "Genres"


class ContentCategory(models.Model):
    name = models.CharField("Category", max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class ContentStatistics(models.Model):
    number_of_views = models.IntegerField("Number of views")
    number_of_likes = models.IntegerField("Number of likes")
    number_of_dislikes = models.IntegerField("Number of dislikes")

    def __str__(self):
        return str(self.number_of_views)

    class Meta:
        verbose_name = "Statistic"
        verbose_name_plural = "Statistics"


class ContentPost(models.Model):
    title = models.CharField("Title", max_length=50)
    description = models.TextField("Description")
    url = models.SlugField(max_length=130, unique=True)

    preview = models.ForeignKey(Preview, on_delete=models.SET_NULL, null=True)
    video = models.ForeignKey(Video, on_delete=models.SET_NULL, null=True)

    genres = models.ManyToManyField(ContentGenre)
    category = models.ManyToManyField(ContentCategory)
    statistics = models.OneToOneField(ContentStatistics, on_delete=models.CASCADE, null=True, default=None)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"


class Channel(models.Model):
    title = models.CharField("Title", max_length=50)
    description = models.TextField("Description")
    creation_date = models.DateTimeField(auto_now_add=True)

    # user_id = TODO:

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Channel"
        verbose_name_plural = "Channels"


class Playlist(models.Model):
    title = models.CharField("Title", max_length=50)
    channel = models.ForeignKey(Channel, on_delete=models.SET_NULL, null=True)
    content_posts = models.ManyToManyField(ContentPost, related_name="content_posts")

    def number_of_posts(self):
        return self.content_posts.count()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Playlist"
        verbose_name_plural = "Playlists"


class PostComment(models.Model):
    # user_id = TODO:

    text = models.TextField("Description")
    creation_date = models.DateTimeField()
    content_post = models.ForeignKey(ContentPost, on_delete=models.SET_NULL, null=True)
    reply_comment = models.ForeignKey("self", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.creation_date

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"
