from django.shortcuts import render, get_object_or_404
from .models import Event, Banner, AboutUs
from .forms import ContactForm
# Create your views here.
def home(request):
    banner = Banner.objects.last()  # Get the latest banner
    about = AboutUs.objects.last()  # Get the latest About Us entry
    events = Event.objects.all()
    return render(request, 'main/home.html', {'events': events,'banner': banner,'about': about})

def events(request):
    events = Event.objects.all()
    return render(request, 'main/events.html', {'events': events})

def event_detail(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    return render(request, 'main/event_detail.html', {'event': event})

def contact(request):
    form = ContactForm()
    return render(request, 'main/contact.html', {'form': form})

def culture(request):
    return render(request, 'main/culture.html',{'culture': culture})