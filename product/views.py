from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect

from product.models import CommentForm, Comment
# Create your views here.

def product(request):
    return HttpResponse("product sayfası")

@login_required(login_url = '/login')
def addcomment(request, id):
    url = request.META.get('HTTP_REFERER')  #GET LAST URL
    if request.method == 'POST': #form Post edildiyse
        form = CommentForm(request.POST)
        if form.is_valid():
            current_user=request.user #Access User Session information

            data = Comment() #model ile bğlantı kur
            data.user_id = current_user.id
            data.product_id = id
            data.subject = form.cleaned_data['subject']
            data.comment = form.cleaned_data['comment']
            data.rate = form.cleaned_data['rate']
            data.ip = request.META.get('REMOTE_ADDR') #client computer ip address
            data.save()  #veritabanına kaydet
            messages.success(request, "Yorumunuz Başarı ile gönderilmişdir. Teşekkür ederiz")
            return HttpResponseRedirect(url)
            #return HttpResponse("Kaydedildi")
    messages.warning(request, "Yorumunuz gönderilmedi" )
    return HttpResponseRedirect(url)

