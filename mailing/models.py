from django.db import models


class MailQueue(models.Model):
    email_from = models.EmailField()
    email_to = models.EmailField()
    is_send = models.BooleanField(default=False)
    subject = models.CharField(max_length=255)
    body = models.TextField()
    is_html = models.BooleanField(default=False)

    def __unicode__(self):
        return u'MailQueue #%s' % self.id
