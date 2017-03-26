from django.conf.urls import url

from sedastrela_is.event.admin_views import send_email_notification


urlpatterns = [
    url(r'^send_email_notifications/(?P<event_id>\d+)/$', send_email_notification, name='send_email_notification'),
]
