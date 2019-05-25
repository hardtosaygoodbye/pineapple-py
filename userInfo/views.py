from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *
from django.http import Http404
import requests
import json
from .WXBizDataCrypt import WXBizDataCrypt

def token2user(token):
    try:
        authority = Authority.objects.get(token = token)
    except:
        raise Http404
    return authority.user

def request2user(request):
    token = request.META.get('HTTP_AUTHORIZATION')
    if len(token) == 0:
        raise Http404
    token = token.split(' ')[1]
    user = token2user(token)
    return user

class MsgCodeView(APIView):
    def randomCode(self):
        seeds = "1234567890"
        random_str = []
        for i in range(6):
            random_str.append(choice(seeds))
        return "".join(random_str)
    def post(self, request):
        phone = request.data.get('phone')
        if len(phone) != 11:
            return Response({'detail': '手机号格式错误'}, 400)
        msgCode = MsgCode(phone = phone, code = self.random_str)
        msgCode.save()
        return Response({
            'code': 0,
            'detail': '验证码发送成功'
        })

# 验证短信验证码
class VerifyMsgCodeView(APIView):
    def post(self, request):
        phone = request.data.get('phone')
        code = request.data.get('code')
        msgCodes = MsgCode.objects.filter(phone = phone, code = code)
        if len(msgCodes) != 1:
            return Response({'detail': '验证码错误'}, 400)
        users = User.objects.filter(phone = phone)
        if len(users) == 1:
            serializer = UserSerializer(users[0])
            return Response({
                'code': 0,
                'detail': '登录成功',
                'user': serializer.data,
                'needSignUp': 0
            })
        else:
            return Response({
                'code': 0,
                'detail': '验证码正确，去注册',
                'needSignUp': 1
            })

# 学校列表
class SchoolView(APIView):
    def get(self, request):
        schools = School.objects.all()
        serializers = SchoolSerializer(schools, many = True)
        return Response({
            'code': 0,
            'schools': serializers.data
        })

# 注册接口
class UserView(APIView):
    def post(self, request):
        phone = request.data.get('phone')
        serializer = UserSerializer(data = request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, 400)
        serializer.save()
        try:
            user = User.objects.get(phone = phone)
        except:
            return Response({'detail': 'user not found'}, 400)
        authority = Authority(user = user)
        authority.save()
        return Response({
            'code': 0,
            'detail': '注册成功',
            'token': authority.token
        })

# 修改学校
class ChangeSchoolView(APIView):
    def post(self, request):
        schoolID = request.data.get('schoolID')
        try:
            school = School.objects.get(pk = int(schoolID))
        except:
            return Response({'detail': '未找到该学校'}, 400)
        user = request2user(request)
        user.school = school
        user.save()
        return Response({
            'code': 0,
            'detail': '修改成功'
        })

# 微信登录
class WechatSignInView(APIView):
    def post(self, request):
        code = request.data.get('code')
        iv = request.data.get('iv')
        encryptedData = request.data.get('encryptedData')
        nickName = request.data.get('nickName')
        avatarUrl = request.data.get('avatarUrl')
        gender = request.data.get('gender')
        appid = 'wxa0f1afb67ee6a023'
        secret = '07d9750a14602a7dd245aa6092f9c987'
        params = {
            'appid': appid,
            'secret': secret, 
            'js_code': code,
            'grant_type': 'authorization_code'
        }
        r = requests.get(url = 'https://api.weixin.qq.com/sns/jscode2session', params = params)
        session_key = r.json().get('session_key')
        # openid = r.json().get('openid')
        pc = WXBizDataCrypt(appid, session_key)
        try:
            userInfo = pc.decrypt(encryptedData, iv)
            phone = userInfo.get('phoneNumber')
            print(userInfo)
        except:
            print('wx error')
            return Response({'detail': '系统异常'}, 400)
        users = User.objects.filter(phone = phone)
        user = None
        if len(users) == 0:
            user = User(
                phone = phone,
                nickName = nickName,
                avatarUrl = avatarUrl,
                gender = gender
            )
            user.save()
        elif len(users) == 1:
            user = users[0]
        else:
            return Response({'detail': '系统异常'}, 400)
        authority = Authority(user = user)
        authority.save()
        needPerfectInfo = 0
        if user.school == None:
            needPerfectInfo = 1
        return Response({
            'code': 0,
            'needPerfectInfo': needPerfectInfo,
            'detail': '微信登录成功',
            'token': authority.token
        })

