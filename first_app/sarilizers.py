from rest_framework import serializers

from saled_products.models import SaledProducts


class SaledProductsSerilizers(serializers.ModelSerializer):
    class Meta:
        model = SaledProducts
        fields = ('__all__')
        