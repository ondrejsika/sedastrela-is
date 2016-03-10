from django.conf import settings
from django.template.loader import render_to_string


class MailTemplateI(object):
    def get_name(self):
        raise NotImplementedError()

    def get_email_from(self):
        raise NotImplementedError()

    def get_subject(self, context):
        raise NotImplementedError()

    def get_body(self, context):
        raise NotImplementedError()

    def get_is_html(self):
        raise NotImplementedError()


class MailTemplate(MailTemplateI):
    name = NotImplemented
    email_from = NotImplemented
    is_html = NotImplemented

    def get_name(self):
        return self.name

    def get_email_from(self):
        return self.email_from

    def get_subject(self, context):
        template = 'mailing/mail_templates/%s/subject.txt' % self.get_name()
        return render_to_string(template, context).replace('\n', '')

    def get_body(self, context):
        template = 'mailing/mail_templates/%s/body.%s' % (
            self.get_name(),
            'html' if self.get_is_html() else 'txt',
        )
        return render_to_string(template, context)

    def get_is_html(self):
        return self.is_html


class EventNotificationMailTemplate(MailTemplate):
    name = 'event_notification'
    email_from = settings.DEFAULT_EMAIL_FROM
    is_html = False


_MAIL_TEMPLATES = [
    EventNotificationMailTemplate,
]

MAIL_TEMPLATES = {mt().get_name(): mt for mt in _MAIL_TEMPLATES}

