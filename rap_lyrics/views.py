from django.shortcuts import render
from .models import Rap 

# Create your views here.
def index(request):
    """The home page"""
    return render(request, 'rap_lyrics/index.html')

def raps(request):
    """Show all the raps"""
    raps = Rap.objects.order_by('date_added')
    context = {'raps': raps}
    return render(request, 'rap_lyrics/raps.html', context)

def rap(request, id):
    """Show a single rap"""
    rap = Rap.objects.get(id=id)
    context = {'rap': rap}
    return render(request, 'rap_lyrics/rap.html', context)



