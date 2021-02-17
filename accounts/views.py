from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.contrib.auth import authenticate, login, logout

from product.models import Category 
from accounts.forms import SignUpForm
from user.forms import UserProfileForm
# Create your views here.

def loginPage(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/')  #also can be redirect
        else:
            messages.info(request, 'Username or Password is incorrect,Please check again')
    
    category = Category.objects.all()
    context = {'category':category}
    return render(request, 'accounts/login.html', context)

def registerPage(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        form = SignUpForm()
        profile_form = UserProfileForm(request.POST)
        if request.method =='POST':
            form = SignUpForm(request.POST)
            profile_form = UserProfileForm(request.POST)
            if form.is_valid() and profile_form.is_valid():
                user = form.save()
                profile = profile_form.save(commit=False)
                profile.user=user
                profile.save()

                user = form.cleaned_data.get('username')
                messages.success(request, 'Profile was created succesfully for ' + user )
                return redirect('login')
                
    category = Category.objects.all()
    context = {'category':category, 'form':form, 'profile_form':profile_form}
    return render(request, 'accounts/register.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')