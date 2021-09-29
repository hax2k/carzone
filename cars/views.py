from django.shortcuts import get_object_or_404, render
from cars.models import Car
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

# Create your views here.


def cars(request):
    all_cars = Car.objects.order_by('-created_date')
    paginator = Paginator(all_cars, 4)
    page = request.GET.get('page')
    paged_cars = paginator.get_page(page)
    model_search = Car.objects.values_list('model', flat=True).distinct()
    city_search = Car.objects.values_list('state', flat=True).distinct()
    year_search = Car.objects.values_list('year', flat=True).distinct()
    body_style_search = Car.objects.values_list(
        'body_style', flat=True).distinct()
    transmission_type = Car.objects.values_list(
        'transmission', flat=True).distinct()
    data = {
        'cars': paged_cars,
        'all_cars': all_cars,
        'model_search': model_search,
        'city_search': city_search,
        'year_search': year_search,
        'body_style_search': body_style_search,
        'transmission_type': transmission_type
    }
    return render(request, 'cars/cars.html', data)


def car_detail(request, id):
    single_car = get_object_or_404(Car, pk=id)
    data = {
        'single_car': single_car,
    }
    return render(request, 'cars/car_detail.html', data)


def car_search(request):
    all_cars = Car.objects.order_by('-created_date')
    model_search = Car.objects.values_list('model', flat=True).distinct()
    cars_search = Car.objects.values_list('car_title', flat=True).distinct()
    city_search = Car.objects.values_list('state', flat=True).distinct()
    year_search = Car.objects.values_list('year', flat=True).distinct()
    body_style_search = Car.objects.values_list(
        'body_style', flat=True).distinct()
    transmission_type = Car.objects.values_list(
        'transmission', flat=True).distinct()
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            all_cars = all_cars.filter(description__icontains=keyword)
    if 'model' in request.GET:
        model = request.GET['model']
        if model:
            all_cars = all_cars.filter(model__iexact=model)
    if 'car_title' in request.GET:
        car_title = request.GET['car_title']
        if car_title:
            all_cars = all_cars.filter(car_title__iexact=car_title)
    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            all_cars = all_cars.filter(state__iexact=state)
    if 'year' in request.GET:
        year = request.GET['year']
        if year:
            all_cars = all_cars.filter(year__iexact=year)
    if 'body_style' in request.GET:
        body_style = request.GET['body_style']
        if body_style:
            all_cars = all_cars.filter(body_style__iexact=body_style)
    if 'min_price' in request.GET:
        min_price = request.GET['min_price']
        max_price = request.GET['max_price']
        if max_price:
            all_cars = all_cars.filter(
                price__gte=min_price, price__lte=max_price)
    if 'transmission' in request.GET:
        transmission = request.GET['transmission']
        if transmission:
            all_cars = all_cars.filter(transmission__iexact=transmission)
    data = {
        'all_cars': all_cars,
        'model_search': model_search,
        'cars_search': cars_search,
        'city_search': city_search,
        'year_search': year_search,
        'body_style_search': body_style_search,
        'transmission_type': transmission_type

    }
    return render(request, 'cars/car_search.html', data)
