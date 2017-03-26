from django.conf import settings

from mailing import send_template_email


def send_event_sms_notification(event):
    # TODO: Not implemented yes, just send mail to admins with instruction to manual send
    for email in settings.ADMIN_NOTIFICATION_EMAILS:
        numbers = event.get_sms_notification_numbers()
        numbers = map(lambda x:x.replace(' ', ''), numbers)
        return send_template_email(email, 'sms_event_notification', {
            'event': event,
            'numbers': numbers,
        })
