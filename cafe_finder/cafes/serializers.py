from rest_framework import serializers
from .models import Cafe
from .models import Barrio
from .models import Reviewer

# We create a class that inherits from DRF's ModelSerializer.
class CafeSerializer(serializers.ModelSerializer):
    summary = serializers.SerializerMethodField()
    # The Meta class is where we configure the serializer.
    class Meta:
    # 1. Tell the serializer which model it's based on.
        model = Cafe
        # 2. Define the "whitelist" of fields to include in the API.
        fields = ['id', 'name', 'barrio', 'address', 'rating', 'notes','has_good_medialunas', 'summary']

    def get_summary(self, obj):
        return f"{obj.name} is a {obj.rating}-star cafe."
        

class BarrioSerializer(serializers.ModelSerializer):
    # The Meta class is where we configure the serializer.
    class Meta:
    # 1. Tell the serializer which model it's based on.
        model = Barrio
        # 2. Define the "whitelist" of fields to include in the API.
        fields = ['barrio_name','comuna']

class ReviewerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviewer
        fields = ['name','join_date']