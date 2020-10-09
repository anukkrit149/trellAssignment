from django.contrib import admin
from .models import *


admin.site.register(director)
admin.site.register(movieData)
admin.site.register(timeSlots)
admin.site.register(shows)
admin.site.register(tickets)