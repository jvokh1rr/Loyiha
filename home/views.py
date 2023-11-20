from django.shortcuts import render, redirect

from home.forms import AddAuto, EditAuto
from home.models import Product, Telefon, Carousel, News

from home.models import Phone
from django.core.paginator import (Paginator, PageNotAnInteger, EmptyPage)


def product(request):
    ooo = Product.objects.all()
    context = {
        'ooo': ooo,
    }
    return render(request, 'index.html', context)


def pro(request):
    return render(request, 'index2.html')


def first_page(request):
    auto = Telefon.objects.all()
    uzavto = {
        'auto': auto,
    }
    return render(request, 'first_page.html', uzavto)


def post_jonatish(request):
    return render(request, 'post_jonatish.html')


def addAuto(request):
    if request.method == 'POST':
        form = AddAuto(request.POST)
        if form.is_valid():
            data = Telefon()
            data.nomi = form.cleaned_data['nomi']
            data.rangi = form.cleaned_data['rangi']
            data.narxi = form.cleaned_data['narxi']
            data.save()
            return redirect('first_page')


def edit_auto(request, id):
    auto = Telefon.objects.get(pk=id)
    if request.method == 'POST':
        form = EditAuto(request.POST, instance=auto)
        if form.is_valid():
            form.save()
            return redirect('first_page')
        else:
            return redirect('edit_auto')
    else:
        form = EditAuto(instance=auto)
        context = {
            'form': form,
            'auto': auto,
        }
    return render(request, 'editauto.html', context)


def delate_auto(request, id):
    auto = Telefon.objects.get(pk=id)
    auto.delete()
    return redirect('first_page')
#######################################################################################3

def carousel(request): #main#
    caro = Carousel.objects.all()
    context = {
        'caro': caro
    }
    return render(request, 'carousel.html', context)
########################################################################################

def ckeditorr(request):
    news = News.objects.all()
    context = {
        'news': news
    }
    return render(request, 'ckeditor.html', context)
########################################################################################
def example(request):
    phone = Phone.objects.all()
    paginator = Paginator(phone, 3)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        phone = paginator.page(page)
    except PageNotAnInteger:
        phone = paginator.page(1)
    except EmptyPage:
        phone = paginator.page(paginator.num_pages)
    context = {
        'phone':phone,
    }
    return render(request, 'pagination1.html', context)


