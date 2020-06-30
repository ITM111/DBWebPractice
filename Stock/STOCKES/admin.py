from django.contrib import admin
from .models import Kospi, Kosdaq, Kospi_by_10second, Kosdaq_by_10second
# Register your models here.


@admin.register(Kosdaq)
class KosdaqAdmin(admin.ModelAdmin):
    list_display = (
        'fluctuation',
        'time'
    )

@admin.register(Kospi)
class KospiAdmin(admin.ModelAdmin):
    list_display = (
        'fluctuation',
        'time'
    )


@admin.register(Kospi_by_10second)
class Kospi_by_10secondAdmin(admin.ModelAdmin):
    list_display = (
        'time',
        'price'
    )


@admin.register(Kosdaq_by_10second)
class Kosdaq_by_10secondAdmin(admin.ModelAdmin):
    list_display = (
        'time',
        'price'
    )
