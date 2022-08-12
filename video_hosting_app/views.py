from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from video_hosting_app.models import *
from video_hosting_app.serializers import *

from decouple import config
import base64
import requests

# import decode_jwt
#
#
# def get_tokens(code):
#     TOKEN_ENDPOINT = config('TOKEN_ENDPOINT')
#     REDIRECT_URI = config('REDIRECT_URI')
#     CLIENT_ID = config('CLIENT_ID')
#     CLIENT_SECRET = config('CLIENT_SECRET')
#
#     encode_data = base64.b64encode(bytes(f'{CLIENT_ID}:{CLIENT_SECRET}', 'ISO-8859-1')).decode('ascii')
#
#     headers = {
#         'Content-Type': 'application/x-www-form-urlencoded',
#         'Authorization': f'Basic {encode_data}'
#     }
#
#     body = {
#         'grant_type': 'authorization_code',
#         'client_id': CLIENT_ID,
#         'code': code,
#         'redirect_uri': REDIRECT_URI
#     }
#
#     response = requests.post(TOKEN_ENDPOINT, data=body, headers=headers)
#     id_token = response.json()['id_token']
#
#     user_data = decode_jwt.lambda_handler(id_token)
#
#     if not user_data:
#         return False
#
#     user = {
#         'id_token': id_token,
#         'name': user_data['name'],
#         'email': user_data['email'],
#     }
#
#     return user


class PreviewView(APIView):
    def get(self, request):
        preview = Preview.objects.all()
        preview_serializer = PreviewSerializer(preview, many=True)
        return Response(preview_serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        preview_serializer = PreviewSerializer(data=request.data)
        if preview_serializer.is_valid(raise_exception=True):
            preview_serializer.save()
            return Response(preview_serializer.data, status=status.HTTP_201_CREATED)


class DetailedPreviewView(APIView):
    def get_object(self, pk):
        try:
            return Preview.objects.get(pk=pk)
        except ContentPost.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        preview = self.get_object(pk)
        preview_serializer = PreviewSerializer(preview)
        return Response(preview_serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, pk):
        preview = self.get_object(pk)
        preview_serializer = PreviewSerializer(preview, data=request.data, partial=True)
        if preview_serializer.is_valid(raise_exception=True):
            preview_serializer.save()
            return Response(preview_serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        preview = self.get_object(pk)
        preview.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class VideoView(APIView):
    def get(self, request):
        video = Video.objects.all()
        video_serializer = VideoSerializer(video, many=True)
        return Response(video_serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        video_serializer = VideoSerializer(data=request.data)
        if video_serializer.is_valid(raise_exception=True):
            video_serializer.save()
            return Response(video_serializer.data, status=status.HTTP_201_CREATED)


class DetailedVideoView(APIView):
    def get_object(self, pk):
        try:
            return Video.objects.get(pk=pk)
        except ContentPost.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        video = self.get_object(pk)
        video_serializer = VideoSerializer(video)
        return Response(video_serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, pk):
        video = self.get_object(pk)
        video_serializer = VideoSerializer(video, data=request.data, partial=True)
        if video_serializer.is_valid(raise_exception=True):
            video_serializer.save()
            return Response(video_serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        video = self.get_object(pk)
        video.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ContentPostListView(APIView):
    def get(self, request):
        content_post = ContentPost.objects.all()
        serializer = MainContentPostSerializer(content_post, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        post_serializer = CreateContentPostSerializer(data=request.data)
        if post_serializer.is_valid(raise_exception=True):
            post_serializer.save()
            return Response(post_serializer.data, status=status.HTTP_201_CREATED)


class ContentPostDetailedView(APIView):
    def get_object(self, pk):
        try:
            return ContentPost.objects.get(pk=pk)
        except ContentPost.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        content_post = self.get_object(pk)
        serializer = MainContentPostSerializer(content_post)
        return Response(serializer.data)

    def patch(self, request, pk):
        content_post = self.get_object(pk)
        serializer = MainContentPostSerializer(content_post, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        content_post = self.get_object(pk)
        content_post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PlaylistListView(APIView):
    def get(self, request):
        playlists = Playlist.objects.all()
        playlist_serializer = PlaylistSerializer(playlists, many=True)
        return Response(playlist_serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        playlist_serializer = PlaylistSerializer(data=request.data)
        if playlist_serializer.is_valid(raise_exception=True):
            playlist_serializer.save()
            return Response(playlist_serializer.data, status=status.HTTP_201_CREATED)


class DetailedPlaylistListView(APIView):
    def get_object(self, pk):
        try:
            return Playlist.objects.get(pk=pk)
        except Playlist.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        playlist = self.get_object(pk)
        serializer = PlaylistSerializer(playlist)
        return Response(serializer.data)

    def patch(self, request, pk):
        playlist = self.get_object(pk)
        serializer = PlaylistSerializer(playlist, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        playlist = self.get_object(pk)
        playlist.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ChannelView(APIView):
    def get(self, request):
        channels = Channel.objects.all()
        channels_serializer = ChannelSerializer(channels, many=True)
        return Response(channels_serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        channels_serializer = ChannelSerializer(data=request.data)
        if channels_serializer.is_valid(raise_exception=True):
            channels_serializer.save()
            return Response(channels_serializer.data, status=status.HTTP_201_CREATED)
