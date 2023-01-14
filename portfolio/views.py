from django.shortcuts import render, redirect
from .models import Cards, Image, Project, Gallery, Certificate, About


# Create your views here.
def home_view(request):
    return render(request, 'home.html', {'cards_lang': Cards.objects.all(),
                                         'images': Image.objects.all()})


def about_view(request):
    return render(request, 'about.html', {'about_me': About.objects.all()})


def certificate_view(request):
    return render(request, 'certificates.html', {'degree': Certificate.objects.all()})


def contact_view(request):
    return render(request, 'Contact_me.html')


def gallery_view(request):
    return render(request, 'Gallery.html', {'my_gallery': Gallery.objects.all()})

