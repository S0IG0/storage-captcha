from rest_framework import viewsets

from storage.serializers import CaptchaSerializer
from storage.models import Captcha


class CaptchaViewSet(viewsets.ModelViewSet):
    queryset = Captcha.objects.all()
    serializer_class = CaptchaSerializer
