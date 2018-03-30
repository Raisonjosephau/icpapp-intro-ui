from rest_framework import serializers
from .models import Market


class CreateMarketSerializer(serializers.ModelSerializer):

    class Meta:
        model= Market
        fields='__all__'
