from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError


# Create your models here.

def validate_email_domain(value):
    if not value.endswith('@esprit.tn'):
        raise ValidationError("L'adresse électronique doit appartenir au domaine esprit.tn")


class Participant(AbstractUser) :
    choix = [
        ("étudiant","étudiant"),
        ("enseignant","enseignant"),
        ("doctorant","doctorant"),
        ("chercheur","chercheur")
    ]
    cin = models.CharField(max_length=8,
                           primary_key=True,
                           unique=True,
                           validators=[RegexValidator(regex=r'^\d{8}$', message="Le CIN doit contenir exactement 8 chiffres.")]
                           )
    email = models.EmailField(unique=True,validators=[validate_email_domain])
    participant_catgory = models.CharField(max_length=255,choices=choix)
    username = models.CharField(max_length=255,unique=True)
    USERNAME_FIELD = 'username'
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)