from django import forms
from django.contrib.auth.forms import AuthenticationForm


class AuthenticationKeycloakForm(AuthenticationForm):
    keycloak_redirrect_button = forms.Field
