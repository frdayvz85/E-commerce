from django.db import models
from django.urls import reverse
from django.utils.safestring import mark_safe  #Phtot for admin panel

from django.forms import ModelForm

from django.contrib.auth.models import User

from ckeditor_uploader.fields import RichTextUploadingField

from mptt.models import MPTTModel, TreeForeignKey  # Best category treee



#from django.urls import  path
# Create your models here.

""" class User(models.Model):
    STATUS = (
        ('New', 'Yeni'),
        ('False','Hayır'),
    )
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    role = models.CharField(max_length=50)
    status = models.CharField(max_length=30, choices=STATUS)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
 """

class Category(MPTTModel):
    STATUS = (
        ('True', 'Evet'),
        ('False','Hayır'),
    )
    title = models.CharField(max_length=30)
    keywords = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image = models.ImageField(blank=True, upload_to='images/')
    status = models.CharField(max_length=10, choices=STATUS)
    slug = models.SlugField(null=False,unique=True)
    parent = TreeForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)#best category choice
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class MPTTMeta:
        #level_attr = 'mptt_level'
        order_insertion_by=['title']

    def __str__(self):
        full_path = [self.title]
        k = self.parent
        while k is not None:
            full_path.append(k.title)
            k = k.parent
        return ' -> '.join(full_path[::-1])


    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'slug':self.slug})


class Product(models.Model):
    STATUS = (
        ('True', 'Evet'),
        ('False','Hayır'),
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE) #relation with Category table
    title = models.CharField(max_length=30)
    keywords = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image = models.ImageField(blank=True, upload_to='images/')
    price = models.FloatField()
    amount = models.IntegerField()
    detail = RichTextUploadingField()
    slug = models.SlugField(null=True, unique=True)
    status = models.CharField(max_length=10, choices=STATUS)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    #Show photo in AdminPanel
    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
    image_tag.short_description = 'Image'

    def get_absolute_url(self):
        return reverse('product_detail', kwargs={'slug':self.slug})

class Images(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE) #relation with Product table
    title = models.CharField(max_length=50)
    image = models.ImageField(blank=True, upload_to='images/')

    def __str__(self):
        return self.title

    #Show photo in AdminPanel
    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
    image_tag.short_description = 'Image'
    

class Comment(models.Model):
    STATUS = (
        ('New', 'Yeni'),
        ('True','Evet'),
        ('False','Hayır'),
    )
    product = models.ForeignKey(Product, on_delete=models.CASCADE) #relation with Product table
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    subject = models.CharField(max_length=50)
    comment = models.TextField(max_length=250, blank=True)
    rate = models.IntegerField(blank=True)
    status = models.CharField(max_length=10, choices=STATUS, default='New')
    ip=models.CharField(blank=True, max_length=20)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['subject','comment','rate']
    