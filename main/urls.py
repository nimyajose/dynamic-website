from django.urls import path
from .views import home, events, contact, event_detail,culture

urlpatterns = [
    path('', home, name='home'),
    path('events/', events, name='events'),
    path('events/<int:event_id>/', event_detail, name='event_detail'),
    path('contact/', contact, name='contact'),
    path('culture/', culture, name='culture'),
]
