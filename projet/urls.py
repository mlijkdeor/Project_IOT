from django.contrib import admin
from django.urls import path, include
from core.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('DHT.urls')),
    path('core/', include('core.urls'))
]
