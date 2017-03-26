from django.core.urlresolvers import reverse
from django.conf import settings

from mailing import send_template_email

from sedastrela_is.event.models import Event, Attendee
from sedastrela_is.person.models import Person


def send_event_email(event, template, context):
    """
    Send email to all possible attendees
    """

    without = Attendee.objects.filter(event=event, state=Attendee.NO).values_list('id', flat=True)

    for person in Person.objects.exclude(id__in=without):
        for email in person.get_emails():
            c = {
                'yes_link': reverse('ssis:event:attending', args=(person.token, event.id, 'yes')),
                'no_link': reverse('ssis:event:attending', args=(person.token, event.id, 'no')),
            }
            c.update(context)
            return send_template_email(email, template, c)


def send_event_notification(event):
    return send_event_email(event, 'event_notification', {
        'event': event,
        'SITE_URL_FULL': settings.SITE_URL_FULL,
    })


