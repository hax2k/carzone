from django.shortcuts import render
from .models import Team

# Create your views here.
def home(request):
    context= Team.objects.all()
    data={ 'teams': context, }
    return render(request,'pages/home.html', data)

def about(request):
    context= Team.objects.all()
    data={ 'teams': context, }
    return render(request,'pages/about.html',data)

def services(request):
    return render(request,'pages/services.html')

def contact(request):
    return render(request,'pages/contact.html')

