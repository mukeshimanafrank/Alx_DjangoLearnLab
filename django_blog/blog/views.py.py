from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.auth.models import User

from .forms import RegisterForm, UserUpdateForm, ProfileForm
from .models import Profile

def home(request):
    return render(request, "home.html")  # simple landing page

def register(request):
    if request.user.is_authenticated:
        return redirect("profile")

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()  # hashes password automatically
            # ensure profile exists if using Profile model
            Profile.objects.get_or_create(user=user)
            login(request, user)  # auto-login after registration
            messages.success(request, "Account created successfully. Welcome!")
            return redirect("profile")
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = RegisterForm()

    return render(request, "blog/register.html", {"form": form})

@login_required
def profile(request):
    # Ensure a profile exists if using the Profile model
    Profile.objects.get_or_create(user=request.user)

    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileForm(request.POST, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, "Profile updated.")
            return redirect("profile")
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileForm(instance=request.user.profile)

    context = {"u_form": u_form, "p_form": p_form}
    return render(request, "blog/profile.html", context)
