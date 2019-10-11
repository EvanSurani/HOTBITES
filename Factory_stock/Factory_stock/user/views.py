from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib import auth
from .forms import RegistrationForm, UserUpdateForm
from django.contrib.auth.forms import User
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'Auth/home.html')
    # return HttpResponse('<h1>Page was found</h1>')


def about_us(request):
    return render(request, 'Auth/about_us.html')


def contact_us(request):
    return render(request, 'Auth/contact_us.html')


@login_required
def view_user(request):
    user  = User.objects.all()
    return render(request, 'adminlayout/view_user.html', {'user' : user})


def base_admin(request):
    return render(request, 'adminlayout/base_admin.html')

def base_user(request):
    return render(request, 'adminlayout/base_user.html')

def registration(request):

    if request.method == 'POST':

        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'Auth/registration.html', {"form": form})


@login_required
def profile(request):
    args= {'user': request.user}
    print(request.user)
    return render(request,'Auth/profile.html',args)

@login_required
def update_profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST,instance=request.user)

        if u_form.is_valid():
            u_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
    return render(request, 'Auth/update_profile.html', {'u_form' : u_form})




