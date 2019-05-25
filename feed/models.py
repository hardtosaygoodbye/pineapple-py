from django.db import models
from userInfo.models import *

# Feed流
class Feed(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    topic = models.CharField('话题', max_length = 20)
    content = models.TextField('内容', max_length = 200)
    status = models.IntegerField(default = 0)

# Feed流图片
class FeedImg(models.Model):
    feed = models.ForeignKey(Feed, on_delete = models.CASCADE, related_name="imgs")
    img = models.CharField(max_length = 200)

'''
# 评价
class Comment(models.Model):
    feed = models.ForeignKey(Feed, on_delete = models.CASCADE)
    time = models.DateTimeField(auto_now_add = True)
    content = models.TextField('内容', max_length = 100)
    fromUser = models.ForeignKey(User, on_delete = models.CASCADE, related_name = '+')
    toUser = models.ForeignKey(User, on_delete = models.CASCADE, related_name = '+')
'''
