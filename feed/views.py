from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *
from django.http import Http404
from userInfo.views import request2user
from qiniu import Auth

class FeedView(APIView):
    def get(self, request):
        user = request2user(request)
        feeds = Feed.objects.filter(user__school__area = user.school.area)
        serializers = FeedSerializer(feeds, many = True)
        return Response({
            'code': 0,
            'feeds': serializers.data
        })
    def post(self, request):
        content = request.data.get('content')
        imgArr = request.data.get('imgArr')
        user = request2user(request)
        feed = Feed(user = user, topic = '', content = content)
        feed.save()
        for img in imgArr:
            feedImg = FeedImg(feed = feed, img = img)
            feedImg.save()
        feedSerializer = FeedSerializer(feed)
        return Response({'code': 0, 'feed': feedSerializer.data})

class MyFeedView(APIView):
    def get(self, request):
        user = request2user(request)
        feeds = Feed.objects.filter(user = user)
        serializers = FeedSerializer(feeds, many = True)
        return Response({
            'code': 0,
            'feeds': serializers.data
        })

class FeedDetailView(APIView):
    def get(self, request):
        feedID = request.GET.get('feedID')
        feedID = int(feedID)
        try:
            feed = Feed.objects.get(pk = feedID)
        except:
            return Response({'detail': 'feed not found'}, 404)
        feedSerializer = FeedSerializer(feed)
        return Response({'code': 0, 'feed': feedSerializer.data})

class QiniuTokenView(APIView):
    def get(self, request):
        access_key = 'yqA6ohfWOH0JjyZvdErd4xzng5FUUO--F_lJ6pA9'
        secret_key = 'Vg3KiZQTwSDnEwn6Wz9z1KtnnVvqsUE8wIGId4VF'
        q = Auth(access_key, secret_key)
        bucket_name = 'swiftwhale'
        token = q.upload_token(bucket_name,expires = 3600*24*7)
        return Response({'uptoken':token})
