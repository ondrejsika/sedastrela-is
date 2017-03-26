from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect

from sedastrela_is.event.models import Event, EventNotification


def send_email_notification(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    notification = EventNotification(event=event,
                                     offset=EventNotification.OFFSET_NONE,
                                     channel=EventNotification.CHANNEL_EMAIL)
    notification.send()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


def send_sms_notification(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    notification = EventNotification(event=event,
                                     offset=EventNotification.OFFSET_NONE,
                                     channel=EventNotification.CHANNEL_SMS)
    notification.send()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])
