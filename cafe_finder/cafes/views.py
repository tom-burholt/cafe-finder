from django.shortcuts import render
from rest_framework import viewsets
from .models import Cafe
from .models import Barrio
from .serializers import CafeSerializer
from .serializers import BarrioSerializer

# Create your views here.
class CafeViewSet(viewsets.ReadOnlyModelViewSet):
        # 1. queryset: Defines the collection of objects that this
        #    viewset will operate on. We'll get all cafes, ordered by rating.
        queryset = Cafe.objects.all().order_by('-rating')
        
        # 2. serializer_class: Tells the viewset which serializer to use
        #    when converting the Cafe objects to JSON.
        serializer_class = CafeSerializer

class BarrioViewSet(viewsets.ReadOnlyModelViewSet):
        
        queryset = Barrio.objects.all().order_by('comuna')
        serializer_class = BarrioSerializer