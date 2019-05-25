from django.contrib import admin
from .models import *

admin.site.site_header = '二手商城'
admin.site.site_title = '二手商城后台'

admin.site.register(MsgCode)
admin.site.register(School)
admin.site.register(User)
admin.site.register(Authority)
