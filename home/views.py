from django.shortcuts import render
from .forms import RegistrationForm
from django.http import HttpResponse, HttpResponseRedirect


# Create your views here.

def index(request):
    return render(request, 'pages/home.html')
def review(request):
    return render(request, 'pages/review.html')
def product(request):
    return render(request, 'pages/product.html')
def contact(request):
    return render(request, 'pages/contact.html')
def introduce(request):
    return render(request, 'pages/introduce.html')
def error(request, exception):
    return render(request, 'pages/error.html', {'message': exception})



def register(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    return render(request, 'pages/register.html', {'form': form})