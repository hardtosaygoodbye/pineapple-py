from django.db import models
from uuid import uuid4

# 短信验证码
class MsgCode(models.Model):
    phone = models.CharField('手机号', max_length = 11, primary_key = True)
    code = models.CharField('验证码', max_length = 6)
    def __str__(self):
        return self.phone + ' - ' + self.code

# 学校
class School(models.Model):
    name = models.CharField('学校名称', max_length = 20)
    area = models.IntegerField('片区', default = 0)
    def __str__(self):
        return self.name

# 用户信息表
class User(models.Model):
    phone = models.CharField('手机号', max_length = 11)
    school = models.ForeignKey(School, on_delete = models.SET_NULL, null = True)
    wechat = models.CharField('微信号', max_length = 20, default = None, null = True, blank = True)
    qq = models.CharField('QQ', max_length = 20, default = None, null = True, blank = True)
    nickName = models.CharField('用户名称', max_length = 20, default = '喵呜')
    avatarUrl = models.URLField('头像', max_length = 200, default='')
    gender = models.IntegerField(default = 0)
    def __str__(self):
        return self.phone

# 用户鉴权表
class Authority(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    token = models.UUIDField(default = uuid4)
    def __str__(self):
        return self.user.phone

