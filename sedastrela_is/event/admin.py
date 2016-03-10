from django.contrib import admin

from sedastrela_is.event.models import Event, Attendee, EventNotification


admin.site.register(Event)
admin.site.register(Attendee)
admin.site.register(EventNotification)
