from django.core.mail import send_mail

from mailing.models import MailQueue


def send_queue(limit):
    q = MailQueue.objects.filter(is_send=False)[:limit]
    for mq in q:
        send_mail(mq.subject, mq.body, mq.email_from, (mq.email_to, ))
        mq.is_send = True
        mq.save()
