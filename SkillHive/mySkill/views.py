from django.shortcuts import render, get_object_or_404
from .models import Event

def home(request):
    courses = Event.objects.all()  # Fetch all courses
    return render(request, "home.html", {'courses': courses})  # Pass to template

def event_detail(request, slug):
    event = get_object_or_404(Event, slug=slug)
    return render(request, 'event_detail.html', {'event': event})

def event_list(request):
    events = Event.objects.all()
    return render(request, 'event_list.html', {'events': events})




# Create your views here.
