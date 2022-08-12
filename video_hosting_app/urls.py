from django.urls import path

from video_hosting_app.views import *

urlpatterns = [
    path("upload_preview", PreviewView.as_view()),
    path("api/preview/<int:pk>", DetailedPreviewView.as_view()),
    path("upload_video", VideoView.as_view()),
    path("api/video/<int:pk>", DetailedVideoView.as_view()),
    path("api/content_posts", ContentPostListView.as_view()),
    path("api/content_posts/<int:pk>", ContentPostDetailedView.as_view()),
    path("api/playlists", PlaylistListView.as_view()),
    path("api/playlists/<int:pk>", DetailedPlaylistListView.as_view()),
    path("api/channels", ChannelView.as_view()),
]
