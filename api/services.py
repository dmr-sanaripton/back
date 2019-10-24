from core.models import Form63
from rest_framework.exceptions import ValidationError, NotFound
from django.db import IntegrityError


class Form63Service:
    @classmethod
    def get(cls, **filters):
        try:
            return Form63.objects.get(**filters)
        except Form63.DoesNotExist:
            raise NotFound('Form 63 was not found')
