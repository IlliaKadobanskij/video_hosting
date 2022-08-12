from storages.backends.s3boto3 import S3Boto3Storage


class VideoStorage(S3Boto3Storage):
    bucket_name = "illia-video-hosting"
    location = "videos"


class PreviewStorage(S3Boto3Storage):
    bucket_name = "illia-video-hosting"
    location = "previews"
