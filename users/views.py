from django.shortcuts import render
from users.forms import UserForm


def register(request):
    register_form = UserForm(request.POST or None)
    if request.method == "POST" and register_form.is_valid():
        new_form = register_form.save()
    return render(request, "signup.html", locals())

def login(request):
    return render(request, "signin.html")

def complete(request):
    return render(request, "register_done.html")
