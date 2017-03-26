from django.contrib import admin

from sedastrela_is.event.models import Event, Attendee, EventNotification


class AttendeeInline(admin.TabularInline):
    model = Attendee
    extra = 0


class NotificationInline(admin.TabularInline):
    model = EventNotification
    extra = 0


class EventAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'from_dt',
        'to_dt',
        'price',
    )
    inlines = (
        AttendeeInline,
        NotificationInline,
    )


class AttendeeAdmin(admin.ModelAdmin):
    list_display = (
        'person',
        'event',
        'state',
        'paid',
    )
    list_filter = (
        'person',
        'event',
        'state',
        'paid',
    )


admin.site.register(Event, EventAdmin)
admin.site.register(Attendee, AttendeeAdmin)
admin.site.register(EventNotification)
