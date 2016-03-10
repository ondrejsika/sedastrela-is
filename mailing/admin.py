from django.contrib import admin

from mailing.models import MailQueue


admin.site.register(MailQueue)
