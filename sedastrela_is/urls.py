from django.conf.urls import include, url
from django.views.generic.base import RedirectView


urlpatterns = [
    url(r'^event/', include('sedastrela_is.event.urls', namespace='event')),
    url(r'^$', RedirectView.as_view(url='/admin/')),
]
