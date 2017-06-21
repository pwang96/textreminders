from django.db import models
from django.core.validators import RegexValidator


class User(models.Model):
    name = models.CharField(max_length=30)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the form +9999999999")
    phone_number = models.CharField(validators=[phone_regex], blank=True, max_length=16)

    def __repr__(self):
        return self.name
