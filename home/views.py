import json #auto complete search ajax
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from home.models import Setting, ContactFormu, ContactFormMessage, FAQ
from product.models import Product, Category, Images, Comment
from order.models import ShopCart

from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.contrib.auth.decorators import login_required

from home.forms import SearchForm


# Create your views here.
#@login_required(login_url = '/login')
def index(request):
    current_user = request.user
    setting = Setting.objects.get(pk=1)
    slider = Product.objects.all().order_by('?')[:4]   # 4 dene random slider gösterilecek
    category = Category.objects.all()
    daysproducts = Product.objects.all()[:4]   # 4 dene daysproduct gösterilecek
    lastproducts = Product.objects.all().order_by('-id')[:4]
    randomproducts = Product.objects.all().order_by('?')[:4]
    request.session['cart_items'] = ShopCart.objects.filter(user_id=current_user.id).count() #count item in the shop cart
    # text = "Djangoyu ben seviyorum işi baya kolaylaşıtırıyor"
    # name = "Ferid Eyvazov"
    context = {'setting':setting, 
               'category':category,
               'page':'home',
               'slider':slider,
               'daysproducts':daysproducts,
               'lastproducts':lastproducts,
               'randomproducts':randomproducts}
    return render(request, 'index.html', context)

def about(request):
    setting1 = Setting.objects.get(pk=1)
    category = Category.objects.all()
    # text = "Djangoyu ben seviyorum işi baya kolaylaşıtırıyor"
    # name = "Ferid Eyvazov"
    context = {'setting1':setting1,
               'category':category}
    return render(request, 'about.html', context)

def contact(request):
    category = Category.objects.all()
    if request.method == 'POST':             #form post edildiyse
        form = ContactFormu(request.POST)
        if form.is_valid():
            data = ContactFormMessage()            # model ile baglanti kur
            data.name = form.cleaned_data['name']  #formdan bilgiyi al
            data.email = form.cleaned_data['email']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data['message']
            data.ip = request.META.get('REMOTE_ADDR') #client computer ip address
            data.save()   #veritabanina kaydet
            messages.success(request, "Mesajınız başarı ile gönderilmiştir. Teşekkür ederiz")
            return HttpResponseRedirect('/contact')


    setting = Setting.objects.get(pk=1)
    form = ContactFormu()
    context = {'setting':setting, 'form':form, 'category': category}
    return render(request, 'contact.html', context)

def category_products(request,id,slug):
    category = Category.objects.all()
    categorydata = Category.objects.get(pk=id)
    products = Product.objects.filter(category_id=id)
    context = {
        'products':products,
        'category':category,
        'categorydata':categorydata
    }
    return render(request, 'product.html', context)

def product_detail(request,id,slug):
    category = Category.objects.all()
    product = Product.objects.get(pk=id)
    images = Images.objects.filter(product_id=id)
    comments = Comment.objects.filter(product_id=id, status='True')

    paginator = Paginator(comments, 3)  # Show 3 contacts per page

    page = request.GET.get('page')
    
    comments = paginator.get_page(page)
 
    #mesaj ="Ürün",id,"/",slug
    context = {
        'category':category,
        'product':product,
        'images':images,
        'comments':comments,
        # 'posts': posts

    }
    return render(request, 'product_detail.html', context)


def product_search(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            category = Category.objects.all() #get form data
            query = form.cleaned_data['query'] #formdan bilgiyi al
            catid = form.cleaned_data['catid'] #formdan bilgiyi al
            if catid == 0:
                products = Product.objects.filter(title__icontains = query) #select*from product where title like %query%
            else:
                products = Product.objects.filter(title__icontains = query, category_id=catid) #select*from product where title like %query%
            context = {'products': products,
                       'category':category
                       }
            return render(request, 'products_search.html', context)
    return HttpResponseRedirect('/')

#oto search by jquery
def product_search_auto(request):
    if request.is_ajax():
      q = request.GET.get('term', '')
      product = Product.objects.filter(title__icontains=q)
      results = []
      for rs in product:
        product_json = {}
        product_json = rs.title 
        results.append(product_json)
      data = json.dumps(results)
    else:
      data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)


# faq view
def faq(request):
    faq = FAQ.objects.filter(status=True).order_by('id')
    category = Category.objects.all()
    context = {
               'faq':faq,
               'category':category
               }
    return render(request, 'faq.html', context)