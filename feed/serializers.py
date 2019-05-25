from rest_framework import serializers
from .models import *

class FeedImgSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedImg
        fields = ['img']

class FeedSerializer(serializers.ModelSerializer):
    imgs = serializers.SerializerMethodField()
    class Meta:
        model = Feed
        fields = '__all__'
        depth = 2
    def get_imgs(self, obj):
        return FeedImgSerializer(obj.imgs, many = True).data



