"""This file contains filterset classes for participant application"""
from django_filters import filters, FilterSet
from participant.models import Client
# ---------------------------------------------------------------------------


class ClientListFilter(FilterSet):
    """This filter is used to filter clients by the first name, last name
    and gender if there is a partial match with search parameters"""
    first_name = filters.CharFilter(
        field_name="first_name", lookup_expr='icontains')
    last_name = filters.CharFilter(
        field_name="last_name", lookup_expr='icontains')

    class Meta:
        model = Client
        fields = ['gender']
