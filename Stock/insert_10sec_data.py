import csv
import os
import sys
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Stock.settings")
django.setup()

if sys.argv[1] == "KOSPI":
    data = open('kospi_by_10sec.csv')
    from STOCKES.models import Kospi_by_10second
    reader = csv.reader(data)
    for row in reader:
        Kospi_by_10second.objects.create(time=row[0], price=row[1])
    print("Success")

elif sys.argv[1] == "KOSDAQ":
    data = open('kosdaq_by_10sec.csv')
    from STOCKES.models import Kosdaq_by_10second
    reader = csv.reader(data)
    for row in reader:
        Kosdaq_by_10second.objects.create(time=row[0], price=row[1])
    print("Success")
