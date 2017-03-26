import datetime

from django.db import models


class Event(models.Model):
    from_dt = models.DateTimeField()
    to_dt = models.DateTimeField()
    title = models.CharField(max_length=128)
    text = models.TextField()
    price = models.IntegerField()

    def __unicode__(self):
        return u'%s %s' % (self.title, self.id)

    @property
    def days_left(self):
        return (self.from_dt - datetime.datetime.now()).days + 1

    def get_sms_notification_numbers(self):
        from sedastrela_is.person.models import Person
        without = Attendee.objects.filter(event=self, state=Attendee.NO).values_list('id', flat=True)

        numbers = []
        for person in Person.objects.exclude(id__in=without):
            numbers += person.get_preferred_sms_numbers()

        return numbers


class Attendee(models.Model):
    YES = 'yes'
    NO = 'no'
    STATES = (
        (YES, YES),
        (NO, NO),
    )

    event = models.ForeignKey(Event)
    person = models.ForeignKey('person.Person')
    state = models.CharField(max_length=4, choices=STATES)

    def __unicode__(self):
        return u'%s %s %s' % (self.person, self.event, self.id)


class EventNotification(models.Model):
    OFFSET_NONE = None
    OFFSET_1D = '1d'
    OFFSET_7D = '7d'
    OFFSET_1M = '1m',

    OFFSETS = (
        (OFFSET_NONE, 'Ihned'),
        (OFFSET_1D, '1 den'),
        (OFFSET_7D, '7 dni'),
        (OFFSET_1M, '1 mesic'),
    )

    CHANNEL_EMAIL = 'email'
    CHANNEL_CALL = 'call'
    CHANNEL_SMS = 'sms'

    CHANNELS = (
        (CHANNEL_EMAIL, 'Email'),
        (CHANNEL_CALL, 'Call'),
        (CHANNEL_SMS, 'SMS')
    )

    event = models.ForeignKey(Event)
    is_sent = models.BooleanField(default=False)
    sent_dt = models.DateTimeField(null=True, blank=True)
    offset = models.CharField(max_length=4, choices=OFFSETS, null=True, blank=True)
    channel = models.CharField(max_length=5, choices=CHANNELS)

    class Meta:
        unique_together = ('event', 'offset')

    def __unicode__(self):
        return u'%s %s %s %s #%s' % (self.event, self.channel, self.is_sent, self.offset, self.id)

    def send(self):
        from sedastrela_is.event.email import send_event_notification
        from sedastrela_is.event.sms import send_event_sms_notification

        if self.channel == self.CHANNEL_EMAIL:
            send_event_notification(self.event)

        if self.channel == self.CHANNEL_SMS:
            # TODO: Not implemented yes, just send mail to admins with instruction to manual send
            send_event_sms_notification(self.event)

        self.is_sent = True
        self.sent_dt = datetime.datetime.now()
        self.save()