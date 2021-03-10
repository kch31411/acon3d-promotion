from rest_framework import serializers
from .models import Promotion


class PromotionSerializer(serializers.ModelSerializer):
    participants = serializers.StringRelatedField(many=True)

    class Meta:
        model = Promotion
        fields = ('id', 'title', 'min_seller', 'max_seller', 'start_date', 'end_date', 'participants')
