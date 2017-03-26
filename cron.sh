#!/bin/bash

while true
do
    python manage.py mailing_send_queue
    sleep 60
done
