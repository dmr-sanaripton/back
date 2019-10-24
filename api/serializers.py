from django.contrib.auth import get_user_model
from rest_framework import serializers

from core.models import Form63, Patient

User = get_user_model()


class Form63ViewSerializer(serializers.Serializer):

    id = serializers.IntegerField()
    
class Form63Serializer(serializers.ModelSerializer):

    class Meta:
        model = Form63
        fields = ('__all__')
