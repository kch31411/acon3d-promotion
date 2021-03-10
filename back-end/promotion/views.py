from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Promotion
from .serializers import PromotionSerializer


@api_view(['GET'])
def get(request):
    promotions = Promotion.objects.all()
    serializer = PromotionSerializer(promotions, many=True)
    return Response(serializer.data)
