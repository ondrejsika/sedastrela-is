from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    nick_name = models.CharField(max_length=32, null=True, blank=True)

    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=16, null=True, blank=True)

    mother_name = models.CharField(max_length=32, null=True, blank=True)
    mother_email = models.EmailField(null=True, blank=True)
    mother_phone = models.CharField(max_length=16, null=True, blank=True)

    father_name = models.CharField(max_length=32, null=True, blank=True)
    father_email = models.EmailField(null=True, blank=True)
    father_phone = models.CharField(max_length=16, null=True, blank=True)

    def __unicode__(self):
        return u'%s %s %s %s' % (self.first_name, self.last_name, self.nick_name or '', self.id)
