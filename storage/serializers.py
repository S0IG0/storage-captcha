from rest_framework import serializers

from storage.models import Captcha


class CaptchaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Captcha
        fields = "__all__"
