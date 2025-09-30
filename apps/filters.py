from django_filters import FilterSet, NumberFilter

from apps.models import Product


class ProductFilter(FilterSet):
    price_min = NumberFilter(field_name="price", lookup_expr='gte')
    price_max = NumberFilter(field_name="price", lookup_expr='lte')

    class Meta:
        model = Product
        fields = ('name',)