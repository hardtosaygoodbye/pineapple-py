from rest_framework.serializers import ModelSerializer
from .models import *

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class SchoolSerializer(ModelSerializer):
    class Meta:
        model = School
        fields = '__all__'
