from cars.models import Car
from django.contrib import admin
from django.utils.html import format_html

# Register your models here.


class CarAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html(f'<img src="{object.car_photo.url}" width="60" style="border-radius:100px;" >')

    list_display = ('id', 'thumbnail', 'car_title', 'color', 'created_date', 'is_featured')
    list_display_links = ('id', 'thumbnail', 'car_title')
    search_fields = ('car_title', 'color', 'year')
    list_filter = ('color',)
    list_editable=('is_featured',)


admin.site.register(Car, CarAdmin)
