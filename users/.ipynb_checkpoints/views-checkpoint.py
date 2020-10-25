from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import UserRegistrationForm, LoginForm
from django.contrib.auth.decorators import login_required


def logout(request):
    return render(request, 'logged_out.html')


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request,
                         'register_done.html',
                         {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request,'registration/signup.html',{'user_form': user_form})


@login_required
def dashboard(request):
    return render(request, 'dashboard.html', {'section': 'dashboard'})



