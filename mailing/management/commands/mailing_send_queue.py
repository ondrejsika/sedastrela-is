from django.core.management.base import BaseCommand

from mailing.send_queue import send_queue


class Command(BaseCommand):
    help = 'Run bitnotify cron task defined in bitnotify/cron.py'

    def handle(self, *args, **options):
        send_queue(50)
