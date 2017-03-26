from django.conf.urls import include, url

urlpatterns = [
    url(r'^event/', include('sedastrela_is.event.urls', namespace='event')),
]

