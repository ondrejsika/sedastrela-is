from mailing.models import MailQueue
from mailing.email_templates import MAIL_TEMPLATES


def send_raw_email(email_from, email_to, subject, body, is_html):
    m = MailQueue(email_from=email_from,
                  email_to=email_to,
                  subject=subject,
                  body=body,
                  is_html=is_html)
    m.save()
    return m


def send_template_email(email_to, template_name, context):
    if template_name not in MAIL_TEMPLATES:
        raise Exception('Mail template does not exist')

    mt = MAIL_TEMPLATES[template_name]()

    m = send_raw_email(email_from=mt.get_email_from(),
                       email_to=email_to,
                       subject=mt.get_subject(context),
                       body=mt.get_body(context),
                       is_html=mt.get_is_html())
    return m

