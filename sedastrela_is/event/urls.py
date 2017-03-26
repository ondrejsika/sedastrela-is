from django.conf.urls import include, url

from sedastrela_is.event.views import attending_done_view, attending_view

urlpatterns = [
    url(r'^admin/', include('sedastrela_is.event.admin_urls', namespace='admin')),
    url(r'^attending/(?P<person_token>\w+)/(?P<event_id>\d+)/(?P<state>\w+)/?', attending_view, name='attending'),
    url(r'^attending-done/?', attending_done_view, name='attending_done'),
]
