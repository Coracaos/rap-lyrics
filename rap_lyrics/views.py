from django.shortcuts import render
from .models import Rap 
from .forms import RapForm
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def index(request):
    """The home page"""
    return render(request, 'rap_lyrics/index.html')

def raps(request):
    """Show all the raps"""
    raps = Rap.objects.order_by('date_added')
    context = {'raps': raps}
    return render(request, 'rap_lyrics/raps.html', context)

def rap(request, rap_id):
    """Show a single rap"""
    rap = Rap.objects.get(id=rap_id)
    context = {'rap': rap}
    return render(request, 'rap_lyrics/rap.html', context)

def new_rap(request):
    """Create a new rap"""
    if request.method != 'POST':
        # No data submitted then create a blank form
        form = RapForm()
    else:
        # POST data submitted then process data
        form = RapForm(data=request.POST)
        if form.is_valid():
            new_rap = form.save(commit=False) # commit=False to save the tags 
            new_rap.save() # Save in the db
            form.save_m2m() # Without this next line the tags won't be saved.
            return HttpResponseRedirect(reverse('rap_lyrics:rap', args=[new_rap.id])) # Redirected to the rap page created

    context = {'form': form} 
    return render(request, 'rap_lyrics/new_rap.html', context) # Page for create a new rap

def edit_rap(request, rap_id):   
    """Edit rap"""
    rap = Rap.objects.get(id=rap_id)

    if request.method != 'POST':
        # Initial request, pre-fil form with the current rap
        form = RapForm(instance=rap)
    else:
        # POST data submitted; process data
        form = RapForm(instance=rap, data=request.POST) 
        if form.is_valid():
            rap = form.save(commit=False)
            rap.save()
            form.save_m2m()
            return HttpResponseRedirect(reverse('rap_lyrics:rap', args=[rap.id]))

    context = {'rap': rap, 'form': form}
    return render(request, 'rap_lyrics/edit_rap.html', context)
