import datetime

from mailing import send_template_email

from sedastrela_is.event.models import Event, Attendee, EventNotification
from sedastrela_is.person.models import Person


def send_event_email(event, template, context):
    """
    Send email to all possible attendees
    """

    without = Attendee.objects.filter(event=event, state=Attendee.NO).values_list('id', flat=True)

    for person in Person.objects.exclude(id__in=without):
        for email in person.get_emails():
            return send_template_email(email, template, context)


def send_event_notification(event):
    return send_event_email(event, 'event_notification', {
        'event': event,
    })


def send():
    for event in Event.objects.filter(from_dt__gte=datetime.datetime.now()):
        offset = EventNotification.get_offset(event.days_left)
        if not offset:
            continue
        notification, created = EventNotification.objects.get_or_create(event=event, offset)
        if notification.is_sent == True:
            continue



