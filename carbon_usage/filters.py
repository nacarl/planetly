from django_filters import rest_framework as filters
from carbon_usage.models import Usage


class UsageFilter(filters.FilterSet):
    usage_at_start = filters.DateFilter(field_name='usage_at', lookup_expr='gt')
    usage_at_end = filters.DateFilter(field_name='usage_at',  lookup_expr='lt')

    class Meta:
        model = Usage
        fields = ['usage_at']
