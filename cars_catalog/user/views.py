from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import logout as logout_user, login
from django.contrib.auth.decorators import login_required
from user.forms import CustomUserCreationForm


@login_required
def logout(request):
    logout_user(request)
    return redirect('/user/login/')


def registration(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/user/login/')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration.html', {'form': form})
