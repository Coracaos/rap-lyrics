from django.urls import path
from . import views

app_name = 'rap_lyrics'

urlpatterns = [
    path('', views.index, name='index'), #Home page
    path('raps', views.raps, name='raps'), #Raps page
    path('raps/<int:id>', views.rap, name='rap'), #Raps page
] 