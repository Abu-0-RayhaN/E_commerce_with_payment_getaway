from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from .models import Profile
from .forms import ProfileForm,SignUpForm

def sign_up(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account Created Successfully!")
            return HttpResponseRedirect(reverse('login'))
    return render(request, 'authentication/signup.html', context={'form':form})


def login_user(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('home'))
    return render(request, 'authentication/login.html', context={'form':form})


@login_required

def logout_user(request):
    logout(request)
    messages.warning(request,'Logged out successfully')
    return HttpResponseRedirect(reverse('home'))

@login_required
def UserProfile(request):
    profile = Profile.objects.get(user=request.user)
    form =ProfileForm(instance=profile)
    if request.method == "POST":
        form= ProfileForm(request.POST,instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request,'changes saved!')
            form=ProfileForm(instance=profile)
    return render(request,'authentication/change_profile.html',context={'form':form})

