from django.contrib import admin

from sedastrela_is.event.models import Event, Attendee, EventNotification
from sedastrela_is.person.models import Person


class AttendeeInline(admin.TabularInline):
    model = Attendee
    extra = 0


class NotificationInline(admin.TabularInline):
    model = EventNotification
    extra = 0


class EventAdmin(admin.ModelAdmin):
    def _attending(obj):
        return Attendee.objects.filter(event=obj, state=Attendee.YES).count()

    def _not_attending(obj):
        return Attendee.objects.filter(event=obj, state=Attendee.NO).count()

    def _responders(obj):
        return Attendee.objects.filter(event=obj).count()

    def _remain(obj):
        return Person.objects.count() - Attendee.objects.filter(event=obj).count()

    list_display = (
        'title',
        'from_dt',
        'to_dt',
        'price',
        _attending,
        _not_attending,
        _responders,
        _remain,
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
