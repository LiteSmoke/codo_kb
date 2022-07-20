from .models import TsRecord
from rest_framework import permissions, viewsets
from .serializers import TsRecordSerializer

class TsRecordViewSet(viewsets.ModelViewSet):

    queryset = TsRecord.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = TsRecordSerializer