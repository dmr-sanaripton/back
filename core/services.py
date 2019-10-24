from django.contrib.auth import get_user_model
from rest_framework.exceptions import NotFound


from .models import Patient

class PatientService:

    @classmethod
    def get(cls, **filters):
        try:
            return Patient.objects.get(**filters, )
        except Patient.DoesNotExist:
            raise NotFound('Patient does not exist')
