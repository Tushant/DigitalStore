from django.contrib.auth.models import User

#rest_framework specific
from rest_framework import serializers

from .models import (Store, OpeningHours, Product, ProductImage, StoreCategory,)


class EagerLoadingMixin:
    @classmethod
    def setup_eager_loading(cls, queryset):
        if hasattr(cls, "_SELECT_RELATED_FIELDS"):
            queryset = queryset.select_related(*cls._SELECT_RELATED_FIELDS)
        if hasattr(cls, "_PREFETCH_RELATED_FIELDS"):
            queryset = queryset.prefetch_related(*cls._PREFETCH_RELATED_FIELDS)
        return queryset

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = "__all__"
        read_only_fields = ('updated', )

class OpeningHoursSerializer(serializers.ModelSerializer):
    class Meta:
        model = OpeningHours
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer, EagerLoadingMixin):
    # _PREFETCH_RELATED_FIELDS = ['image',]
    class Meta:
        model = Product
        exclude = ('is_active', )

class StoreSerializer(serializers.ModelSerializer, EagerLoadingMixin):
    _SELECT_RELATED_FIELDS = ['merchant', ]
    # product = ProductSerializer(many=True)
    opening_hour = OpeningHoursSerializer(many=True)
    id = serializers.CharField(source='token', read_only=True)
    class Meta:
        model = Store
        exclude = ('is_active', )
