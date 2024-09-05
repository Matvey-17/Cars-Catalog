from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django import forms
from django.contrib.auth.models import User


class CustomLoginView(LoginView):
    template_name = 'login.html'

    def get_success_url(self):
        return reverse_lazy('product:main')


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super(CustomUserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
