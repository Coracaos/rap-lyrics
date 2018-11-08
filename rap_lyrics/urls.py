from django.urls import path
from . import views

app_name = 'rap_lyrics'

urlpatterns = [
    path('', views.index, name='index'), #Home page
    path('raps', views.raps, name='raps'), #Raps page
    path('raps/<int:rap_id>', views.rap, name='rap'), #Rap page
    path('new_rap', views.new_rap, name='new_rap'), #Page for create a new rap
] 