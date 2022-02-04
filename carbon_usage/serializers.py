from django.contrib.auth.models import User
from rest_framework import serializers
from carbon_usage.models import UsageType, Usage


# serializer classes define how models are converted to a json format
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'url', 'url', 'username', 'email', 'groups']


class UsageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Usage
        fields = ['id', 'url', 'user', 'usage_type', 'usage_at', 'amount', 'user']


class UsageTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UsageType
        fields = ['id', 'url', 'name', 'unit', 'factor']
