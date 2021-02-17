from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from order.models import ShopCart, ShopCartForm
from product.models import Category

# Create your views here.

def order(request):
    return HttpResponse("My order")


@login_required(login_url='/login')
def addtocart(request, id):
    url = request.META.get('HTTP_REFERER')  #GET LAST URL
    current_user=request.user #Access User Session information

    checkproduct = ShopCart.objects.filter(product_id=id)
    if checkproduct:
        control = 1 #The product is in the cart
    else:
        control = 0 #The product is not in the cart
        
    if request.method == 'POST': #form Post edildiyse
        form = ShopCartForm(request.POST)
        if form.is_valid():
           if control == 1:
                data = ShopCart() #model ile bğlantı kur
                data.user_id = current_user.id
                data.quantity += form.cleaned_data['quantity']
                data.save()  #veritabanına kaydet
           else:
               data = ShopCart() #model ile bğlantı kur
               data.user_id = current_user.id
               data.product_id=id
               data.quantity = form.cleaned_data['quantity']
               data.save()  #veritabanına kaydet

        request.session['cart_items'] = ShopCart.objects.filter(user_id=current_user.id).count() #count item in the shop cart
        messages.success(request, "Ürün başarı ile sepete eklenmişdir. Teşekkür ederiz")
        return HttpResponseRedirect(url)
        #return HttpResponse("Kaydedildi")
    else:
        if control == 1:
            data = ShopCart.objects.get(product_id=id) #model ile bğlantı kur
            data.quantity = 1
            data.save()  #veritabanına kaydet
        else:
            data = ShopCart() #model ile bğlantı kur
            data.user_id = current_user.id
            data.product_id = id
            data.quantity = 1
            data.save()  #veritabanına kaydet
        request.session['cart_items'] = ShopCart.objects.filter(user_id=current_user.id).count() #count item in the shop cart
        messages.success(request, "Ürün başarı ile sepete eklenmişdir. Teşekkür ederiz")
        return HttpResponseRedirect(url)


    messages.warning(request, "Urün sepete eklemede hata oluştu!, Lütfen tekrar kontrol ediniz")
    return HttpResponseRedirect(url)



@login_required(login_url='/login')
def shopcart(request):
    category = Category.objects.all()
    current_user = request.user
    shopcart = ShopCart.objects.filter(user_id=current_user.id)
    request.session['cart_items'] = ShopCart.objects.filter(user_id=current_user.id).count() #count item in the shop cart

    total = 0
    for rs in shopcart:
        total += rs.product.price*rs.quantity
    
    context = { 
        'shopcart':shopcart,
        'category': category,
        'total': total,
    }
    return render(request, 'myorders.html', context)

@login_required(login_url='/login')
def deletefromcart(request, id):
    ShopCart.objects.filter(id=id).delete()
    current_user = request.user
    request.session['cart_items'] = ShopCart.objects.filter(user_id=current_user.id).count() #count item in the shop cart
    messages.success(request, "Ürün seppetten silinmiştir. Teşekkür ederiz")
    return HttpResponseRedirect("/shopcart")