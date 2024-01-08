#from django.contrib.auth.decorator import login_required
from .forms import NewDht11
from django.shortcuts import render,redirect
from .models import Dht11  # Assurez-vous d'importer le modèle Dht11
from django.utils import timezone
import csv
from django.http import HttpResponse
from django.utils import timezone
from django.http import JsonResponse
from datetime import timedelta
from datetime import datetime

def table(request):
    derniere_ligne = Dht11.objects.all()
    for item in derniere_ligne:
        derniere_date = item.dt
        delta_temps = timezone.now() - derniere_date
        difference_minutes = delta_temps.seconds // 60
        temps_ecoule = ' il y a ' + str(difference_minutes) + ' min'
        if difference_minutes > 60:
            temps_ecoule = 'il y a' + str(difference_minutes // 60) + 'h ' + str(difference_minutes % 60) + 'min'

    return render(request, 'value.html', {'derniere_ligne': derniere_ligne})


def download_csv(request):
    model_values = Dht11.objects.all()
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="dht.csv"'
    writer = csv.writer(response)
    writer.writerow(['id', 'temp', 'hum', 'dt'])
    liste = model_values.values_list('id', 'temp', 'hum', 'dt')
    for row in liste:
        writer.writerow(row)
    return response
#pour afficher navbar de template
def index_view(request):
    return render(request, 'index.html')

#pour afficher les graphes
def graphiqueTemp(request):
    return render(request, 'ChartTemp.html')

#pour afficher les graphes
def graphiqueHum(request):
    return render(request, 'ChartHum.html')
# récupérer toutes les valeur de température et humidity sous forme un #fichier json
def chart_data(request):
    dht = Dht11.objects.all()

    data = {
        'temps': [Dt.dt.strftime("%d/%m/%y") for Dt in dht],
        'temperature': [Temp.temp for Temp in dht],
        'humidity': [Hum.hum for Hum in dht]
    }
    return JsonResponse(data)

#pour récupérer les valeurs de température et humidité de dernier 24h
# et envoie sous forme JSON
def chart_data_jour(request):
    dht = Dht11.objects.all()
    now = timezone.now()

    # Récupérer l'heure il y a 24 heures
    last_24_hours = now - timezone.timedelta(hours=24)

    # Récupérer tous les objets de Module créés au cours des 24 dernières heures
    dht = Dht11.objects.filter(dt__range=(last_24_hours, now))
    data = {
        'temps': [Dt.dt.strftime("%H:%M") for Dt in dht],
        'temperature': [Temp.temp for Temp in dht],
        'humidity': [Hum.hum for Hum in dht]
    }
    return JsonResponse(data)

#pour récupérer les valeurs de température et humidité de dernier semaine
# et envoie sous forme JSON
def chart_data_semaine(request):
    now = timezone.now()

    # Récupérer l'heure il y a 24 heures
    derniere_semaine = now - timezone.timedelta(days=7)

    # filtrer les enregistrements créés depuis le début de la semaine dernière
    dht = Dht11.objects.filter(dt__gte=derniere_semaine)

    data = {
        'temps': [Dt.dt.strftime("%d/%m") for Dt in dht],
        'temperature': [Temp.temp for Temp in dht],
        'humidity': [Hum.hum for Hum in dht]
    }

    return JsonResponse(data)

#pour récupérer les valeurs de température et humidité de dernier moins
# et envoie sous forme JSON
def chart_data_mois(request):
    now = timezone.now()

    # Récupérer l'heure il y a 24 heures
    derniere_semaine = now - timezone.timedelta(days=30)

    # filtrer les enregistrements créés depuis le début de la semaine dernière
    dht = Dht11.objects.filter(dt__gte=derniere_semaine)

    data = {
        'temps': [Dt.dt.strftime("%d/%m") for Dt in dht],
        'temperature': [Temp.temp for Temp in dht],
        'humidity': [Hum.hum for Hum in dht]
    }
    return JsonResponse(data)

#@login_required

def new(request):
    if request.method == 'POST':
        form=NewDht11(request.POST)

        if form.is_valid():
            Dht11= form.save(commit=False)
            Dht11.dt=datetime.now()
            Dht11.save()

            return redirect('core:index')
    else:
        form=NewDht11()

    return render(request, 'DHT/add.html' ,{'form': form})