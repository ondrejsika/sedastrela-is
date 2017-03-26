from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from sedastrela_is.event.models import Event, Attendee
from sedastrela_is.person.models import Person


def attending_view(request, person_token, event_id, state):
    assert state in (Attendee.YES, Attendee.NO), state

    person = get_object_or_404(Person, token=person_token)
    event = get_object_or_404(Event, id=event_id)
    attendee, _ = Attendee.objects.get_or_create(event=event, person=person)
    attendee.state = state
    attendee.save()
    return HttpResponseRedirect(reverse('ssis:event:attending_done'))


def attending_done_view(request):
    return render(request, 'event/attending_done.html')
