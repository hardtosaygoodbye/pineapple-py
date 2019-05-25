from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^msgCodes/$', MsgCodeView.as_view()),
    url(r'^schools/$', SchoolView.as_view()),
    url(r'^users/$', UserView.as_view()),
    url(r'^wechatSignIn/$', WechatSignInView.as_view()),
    url(r'^changeSchool/$', ChangeSchoolView.as_view()),
]
