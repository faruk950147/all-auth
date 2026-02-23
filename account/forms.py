from django import forms
from allauth.account.forms import (
    SignupForm,
    LoginForm   
)

class CustomSignupForm(SignupForm):
    def save(self, request):
        """ Override the save method to set the user as inactive until email verification. """
        user = super().save(request)
        user.is_active = False
        user.save()
        return user

class CustomLoginForm(LoginForm):
    def confirm_login_allowed(self, user):
        """ Check if the user's account is active before allowing login. """
        if not user.is_active:
            raise forms.ValidationError(
                "Your account is inactive. Please verify your email."
            )
        return super().confirm_login_allowed(user)