import csv
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE","Stock.settings")
django.setup()

from STOCKES.models import Kospi, Kosdaq

data = open('db.kospi_time.csv')
reader = csv.reader(data)
bulk_list = []

for row in reader:
    bulk_list.append(Kospi(fluctuation=row[1], time = row[0]))

Kospi.objects.bulk_create(bulk_list)

data = open('db.kosdaq_time.csv')

reader = csv.reader(data)
bulk_list = []

for row in reader:
    bulk_list.append(Kosdaq(fluctuation=row[1], time = row[0]))

Kosdaq.objects.bulk_create(bulk_list)
