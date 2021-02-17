from django.shortcuts import render
from django.http import HttpResponse

from product.models import Category 
from user.models import UserProfile



def userProfile(request):
    category = Category.objects.all()
    current_user = request.user.userprofile
    profile = UserProfile.objects.get(pk=current_user.id)
    context = {
        'category':category,
        'profile':profile,
    }
    return render(request, 'users/user_profile.html', context)
