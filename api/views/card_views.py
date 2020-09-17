from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from ..models.card import Card
from ..serializers import CardSerializer

# Create your views here.
class Cards(APIView):
    def get(self, request):
        """Index Request"""
        print(request)
        cards = Card.objects.all()[:10]
        data = CardSerializer(cards, many=True).data
        return Response(data)

    serializer_class = CardSerializer
    def post(self, request):
        """Post request"""
        print(request.data)
        card = CardSerializer(data=request.data['card'])
        if card.is_valid():
            card.save()
            return Response(card.data, status=status.HTTP_201_CREATED)
        else:
            return Response(card.errors, status=status.HTTP_400_BAD_REQUEST)

class CardDetail(APIView):
    def get(self, request, pk):
        """Show request"""
        card = get_object_or_404(Card, pk=pk)
        data = CardSerializer(card).data
        return Response(data)

    def patch(self, request, pk):
        """Update Request"""
        card = get_object_or_404(Card, pk=pk)
        ms = CardSerializer(card, data=request.data['card'], partial=True)
        if ms.is_valid():
            ms.save()
            return Response(ms.data)
        return Response(ms.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        """Delete Request"""
        card = get_object_or_404(Card, pk=pk)
        card.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
