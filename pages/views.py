from django.shortcuts import render
from cars.models import Car
from .models import Team

# Create your views here.


def home(request):
    context = Team.objects.all()
    feature_car = Car.objects.order_by(
        '-created_date').filter(is_featured=True)
    all_cars = Car.objects.order_by('-created_date')
    model_search = Car.objects.values_list('model', flat=True).distinct()
    city_search = Car.objects.values_list('state', flat=True).distinct()
    year_search = Car.objects.values_list('year', flat=True).distinct()
    body_style_search = Car.objects.values_list(
        'body_style', flat=True).distinct()
    data = {'teams': context,
            'feature_car': feature_car,
            'all_cars': all_cars,
            'model_search': model_search,
            'city_search': city_search,
            'year_search': year_search,
            'body_style_search': body_style_search
            }
    return render(request, 'pages/home.html', data)


def about(request):
    context = Team.objects.all()

    data = {'teams': context, }
    return render(request, 'pages/about.html', data)


def services(request):
    return render(request, 'pages/services.html')


def contact(request):
    return render(request, 'pages/contact.html')
