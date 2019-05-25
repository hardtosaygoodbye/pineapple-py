from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^feeds/$', FeedView.as_view()),
    url(r'^myFeeds/$', MyFeedView.as_view()),
    url(r'^qiniuToken/$', QiniuTokenView.as_view()),
]
