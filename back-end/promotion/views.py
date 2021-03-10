from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Promotion, Seller
from .serializers import PromotionSerializer


@api_view(['GET'])
def get(request):
    promotions = Promotion.objects.prefetch_related('participants').all()
    serializer = PromotionSerializer(promotions, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def apply(request):
    try:
        requester = Seller.objects.get(brand_id=request.data.get('brand_id'))
        promotion = Promotion.apply(request.data.get('id'), requester)

        # TODO: serialize 중에 db에서 participants를 불필요하게 한차례 더 조회함.
        return Response(PromotionSerializer(promotion).data, status=status.HTTP_200_OK)
    except ValueError as e:
        return Response(str(e), status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response(str(e), status=status.HTTP_400_BAD_REQUEST)
