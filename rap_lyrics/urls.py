from django.urls import path
from . import views

app_name = 'rap_lyrics'

urlpatterns = [
    path('', views.index, name='index'), # Home page
    path('raps', views.raps, name='raps'), # Raps page
    path('raps/<int:rap_id>', views.rap, name='rap'), # Rap page
    path('new_rap', views.new_rap, name='new_rap'), # Page for create a new rap
    path('edit_rap/<int:rap_id>', views.edit_rap, name='edit_rap') # Page for edit rap
] 