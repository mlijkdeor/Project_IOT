from django.urls import path, include
from . import views
from . import api

app_name='DHT'

urlpatterns = [
    path("api",api.dhtser,name='json'),
    path('download_csv/', views.download_csv, name='download_csv'),
    path('', include('core.urls')),
    path('table/', views.table, name='table'),
    path('myChartTemp/',views.graphiqueTemp,name='myChart'),
    path('myChartHum/',views.graphiqueHum,name='myChart'),
    path ('chart-data/',views.chart_data, name='chart-data'),
    path('chart-data-jour/',views.chart_data_jour,name='chart-data-jour'),
    path('chart-data-semaine/',views.chart_data_semaine,name='chart-data-semaine'),
    path('chart-data-mois/',views.chart_data_mois,name='chart-data-mois'),
    path('new/', views.new , name='new'),





]
