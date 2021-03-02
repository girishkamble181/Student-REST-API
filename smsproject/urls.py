
from django.contrib import admin
from django.urls import path
from smsapp.views import stuop


urlpatterns = [
    path('admin/', admin.site.urls),
    path('stuop/',stuop),
    path('stuop/<int:id>',stuop),
]
