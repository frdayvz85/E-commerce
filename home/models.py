from django.db import models

from ckeditor_uploader.fields import RichTextUploadingField

from django.forms import ModelForm, TextInput, Textarea  #THis is for ContactForm
# Create your models here.

class Setting(models.Model):
    STATUS = (
        ('True', 'Evet'),
        ('False','Hayır'),
    )
    title = models.CharField(max_length=30)
    keywords = models.CharField(blank=True, max_length=25)
    description = models.CharField(blank=True, max_length=25)
    company = models.CharField(max_length=20)
    address = models.CharField(max_length=30)
    phone = models.CharField(blank=True, max_length=15)
    fax = models.CharField(blank=True, max_length=30)
    email = models.CharField(max_length=15)
    smtpserver = models.CharField(blank=True, max_length=30)
    smtpmail = models.CharField(blank=True, max_length=30)
    smtppassword = models.CharField(blank=True, max_length=30)
    smtpport = models.CharField(blank=True, max_length=30)
    icon = models.ImageField(blank=True, upload_to='images/')
    facebook = models.CharField(blank=True, max_length=30)
    instagram = models.CharField(blank=True, max_length=30)
    twitter = models.CharField(max_length=30)
    abouts = RichTextUploadingField()
    contact = RichTextUploadingField(blank=True)
    references = RichTextUploadingField()
    status = models.CharField(max_length=10, choices=STATUS)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return self.title


class ContactFormMessage(models.Model):
    STATUS = (
        ('New', 'New'),
        ('Read', 'Read'),
    )
    name = models.CharField(blank=True, max_length=20)
    email = models.CharField(blank=True, max_length=50)
    subject = models.CharField(blank=True, max_length=50)
    message = models.CharField(blank=True, max_length=255)
    status = models.CharField(max_length=20, choices=STATUS, default='New')
    ip = models.CharField(blank=True, max_length=20)
    note = models.CharField(blank=True, max_length=200)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class ContactFormu(ModelForm):
    class Meta:
        model = ContactFormMessage
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name':    TextInput(attrs={'class': 'input', 'placeholder': 'Name & Surname'}),
            'subject': TextInput(attrs={'class': 'input', 'placeholder': 'Subject'}),
            'email':   TextInput(attrs={'class': 'input', 'placeholder': 'Email Adress'}),
            'message': Textarea(attrs={'class': 'input', 'placeholder': 'Your Message', 'rows':'10'}),
        }    

#Faq Model
class FAQ(models.Model):
    STATUS = (
        ('True', 'Evet'),
        ('False','Hayır'),
    )
    orderrnumber = models.IntegerField()
    question = models.CharField(max_length=250)
    answer = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return self.question