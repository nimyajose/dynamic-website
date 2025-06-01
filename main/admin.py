from django.contrib import admin
from .models import Event, AboutUs
from .models import Banner
# Register your models here.
admin.site.register(Event)
admin.site.register(Banner)
admin.site.register(AboutUs)