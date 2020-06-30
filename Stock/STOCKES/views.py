from django.shortcuts import render
from django.core import serializers
from datetime import datetime, timedelta
import json
from django.http import JsonResponse
from .models import Kospi, Kosdaq, Kospi_by_10second, Kosdaq_by_10second


def chart(request):
    return render(request, 'chart.html')

def chart_data_kospi(request):
    dataset = Kospi.objects.all().order_by('time')
    kospis =[]
    for stock in dataset:
        time = (stock.time.hour*3600 + stock.time.minute*60 + stock.time.second)*1000
        kospis.append([time, stock.fluctuation*100])
        
    return JsonResponse(kospis, safe=False)

def chart_data_kosdaq(request):
    dataset = Kosdaq.objects.all().order_by('time')
    kosdaqs = []
    for stock in dataset:
        time = (stock.time.hour*3600 + stock.time.minute*60 + stock.time.second)*1000
        kosdaqs.append([time, stock.fluctuation*100])
    return JsonResponse(kosdaqs, safe=False)


def search(request):
    date = request.GET.get("date")
    index = request.GET.get("index")
    if not date or not index:
        return render(request, 'search.html')
    date = datetime.strptime(date, "%Y-%m-%d")
    if index == "KOSPI":
        index = Kospi_by_10second
    elif index == "KOSDAQ":
        index = Kosdaq_by_10second
    else:
        return render(request, 'search.html')
    return render(request, 'search.html', {'indexes': index.objects.filter(time__gt=date, time__lt=date+timedelta(days=1))})

