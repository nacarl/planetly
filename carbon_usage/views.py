from django.contrib.auth.models import User
from rest_framework import viewsets, filters
from rest_framework import permissions
from carbon_usage.models import Usage, UsageType
from carbon_usage.serializers import UserSerializer, UsageSerializer, UsageTypeSerializer
from carbon_usage.filters import UsageFilter


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class UsageViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows usages to be viewed or edited.
    """
    queryset = Usage.objects.all()
    serializer_class = UsageSerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_class = UsageFilter
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['usage_type']


class UsageTypeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows usage types to be viewed or edited.
    """
    queryset = UsageType.objects.all()
    serializer_class = UsageTypeSerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_fields = ['name', 'unit', 'factor']
