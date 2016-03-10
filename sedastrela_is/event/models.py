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
