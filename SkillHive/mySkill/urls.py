from django.contrib import admin
from django.urls import path
from .views import home, event_detail, event_list

urlpatterns = [
    path('', home, name='home'),  # Home page (lists courses)
    path('event/<slug:slug>/', event_detail, name='event_detail'),
     path('events/', event_list, name='event_list'), # Individual course detail page
]
