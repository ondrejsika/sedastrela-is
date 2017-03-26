from django.conf.urls import include, url

urlpatterns = [
    url(r'^admin/', include('sedastrela_is.event.admin_urls', namespace='admin')),
]
