from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator, EmailValidator, MinValueValidator


class Blog(models.Model):
    name = models.CharField(max_length=150)
    user_id = models.PositiveIntegerField(validators=[MinValueValidator(limit_value=0,)],)
    phone_number = models.CharField(
        max_length=20,
        validators=[
            RegexValidator(
                regex=r'^(\+98|0)?9\d{9}$',
                message="Please enter a valid phone number"
            ),
        ]
    )
    email = models.CharField(
        max_length=150,
        validators=[
            EmailValidator(),
        ]
    )
    address = models.TextField()
    purchase = models.CharField(max_length=150)
    purchase_id = models.PositiveIntegerField(validators=[MinValueValidator(limit_value=0,)],)
    datetime = models.DateTimeField()

    