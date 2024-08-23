from django.db import models


class Captcha(models.Model):
    image = models.FileField(upload_to='images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
