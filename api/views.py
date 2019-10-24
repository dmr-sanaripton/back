from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from api.serializers import Form63Serializer, Form63ViewSerializer
from rest_framework import status

from api.services import Form63Service
from core.services import PatientService


INVALID_INPUT = "Invalid input"

class Form63View(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):

        serializer = Form63ViewSerializer(data=request.data, many=False)

        if not serializer.is_valid():
            return Response(data={'message': INVALID_INPUT, 'errors': serializer.errors},
                                                        status=status.HTTP_406_NOT_ACCEPTABLE)

        patient = PatientService.get(
            id=serializer.validated_data.get('id')
        )

        form = Form63Service.get(patient=patient)

        return Response(Form63Serializer(form).data, status=status.HTTP_200_OK)
