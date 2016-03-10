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
    OFFSET_1D = '1d'
    OFFSET_7D = '7d'
    OFFSET_1M = '1m',

    OFFSETS = (
        (OFFSET_1D, '1 den'),
        (OFFSET_7D, '7 dni'),
        (OFFSET_1M, '1 mesic'),
    )

    event = models.ForeignKey(Event)
    is_sent = models.BooleanField(default=False)
    offset = models.CharField(max_length=4, choices=OFFSETS)

    class Meta:
        unique_together = ('event', 'offset')

    def __unicode__(self):
        return u'%s %s %s #%s' % (self.event, self.is_sent, self.offset, self.id)
