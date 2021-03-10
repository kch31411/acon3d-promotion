from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Promotion, Seller
from .serializers import PromotionSerializer


@api_view(['GET'])
def get(request):
    promotions = Promotion.objects.all()
    serializer = PromotionSerializer(promotions, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def apply(request):
    try:
        requester = Seller.objects.get(brand_id=request.data.get('brand_id'))
        promotion = Promotion.objects.get(id=request.data.get('id'))

        promotion.apply(requester)

        return Response(PromotionSerializer(promotion).data, status=status.HTTP_200_OK)
    except ValueError as e:
        return Response(str(e), status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response(str(e), status=status.HTTP_400_BAD_REQUEST)
