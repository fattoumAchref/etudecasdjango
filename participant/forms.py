from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Participant

class ParticipantRegistrationForm(UserCreationForm):
    class Meta:
        model = Participant
        fields = ['username', 'cin', 'email', 'participant_catgory', 'first_name', 'last_name']

class ParticipantLoginForm(AuthenticationForm):
    username = forms.CharField(label="Nom d'utilisateur")
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)
