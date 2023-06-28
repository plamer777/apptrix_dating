"""This file contains filterset classes for participant application"""
from django_filters import filters, FilterSet
from participant.models import Client
# ---------------------------------------------------------------------------


class ClientListFilter(FilterSet):
    """This filter is used to filter clients by the first name, last name,
     gender and distance"""
    first_name = filters.CharFilter(
        field_name="first_name", lookup_expr='icontains')
    last_name = filters.CharFilter(
        field_name="last_name", lookup_expr='icontains')
    distance = filters.NumberFilter(method='filter_distance')

    def filter_distance(self, queryset, name, value):
        """This method"""
        user = self.request.user
        queryset = queryset.exclude(user__pk=user.pk)
        return queryset.filter(distance__lte=value)

    class Meta:
        model = Client
        fields = ['gender']
