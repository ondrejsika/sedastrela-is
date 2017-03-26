from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    nick_name = models.CharField(max_length=32, null=True, blank=True)

    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=16, null=True, blank=True)
    facebook = models.CharField(max_length=256, null=True, blank=True)

    mother_name = models.CharField(max_length=32, null=True, blank=True)
    mother_address = models.TextField(null=True, blank=True)
    mother_email = models.EmailField(null=True, blank=True)
    mother_email_preferred = models.BooleanField(default=True)
    mother_phone = models.CharField(max_length=16, null=True, blank=True)
    mother_phone_call_preferred = models.BooleanField(default=False)
    mother_phone_sms_preferred = models.BooleanField(default=True)
    mother_facebook = models.CharField(max_length=256, null=True, blank=True)
    mother_facebook_preferred = models.BooleanField(default=True)

    father_name = models.CharField(max_length=32, null=True, blank=True)
    father_address = models.TextField(null=True, blank=True)
    father_email = models.EmailField(null=True, blank=True)
    father_email_preferred = models.BooleanField(default=True)
    father_phone = models.CharField(max_length=16, null=True, blank=True)
    father_phone_call_preferred = models.BooleanField(default=False)
    father_phone_sms_preferred = models.BooleanField(default=True)
    father_facebook = models.CharField(max_length=256, null=True, blank=True)
    father_facebook_preferred = models.BooleanField(default=True)

    def __unicode__(self):
        return u'%s %s %s %s' % (self.first_name, self.last_name, self.nick_name or '', self.id)

    def get_emails(self):
        """
        Returns list of all available emails for notifications.
        """
        return filter(None, (self.email, self.mother_email, self.father_email))
