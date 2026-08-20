from django.db.models import F
from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.decorators import action, api_view
from rest_framework.response import Response

from cafes import utils

from .models import Barrio, Cafe, Review, Reviewer
from .serializers import (BarrioSerializer, CafeSerializer, ReviewerSerializer,
                          ReviewSerializer)


class CafeViewSet(viewsets.ModelViewSet):

    serializer_class = CafeSerializer
    queryset = Cafe.objects.all()

    @action(detail=True, methods=["post"])
    def recommend(self, request, pk):
        cafe = self.get_object()
        cafe.recommendation_count = F("recommendation_count") + 1
        cafe.save()
        return Response(
            {
                "message": f"Successfully recommended {cafe.name}!",
                "recommendation_count": cafe.recommendation_count,
            },
        )

    @action(detail=False, methods=["get"])
    def top_rated(self, request):
        cafes = Cafe.objects.filter(rating=5)
        serializer = self.get_serializer(cafes, many=True)
        return Response(serializer.data)

    def perform_create(self, serializer):
        cafe = serializer.save()
        utils.send_new_cafe_notification(cafe.name)


class BarrioViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Barrio.objects.all().order_by("name")
    serializer_class = BarrioSerializer


class ReviewerViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Reviewer.objects.all()
    serializer_class = ReviewerSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
