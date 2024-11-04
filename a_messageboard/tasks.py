from datetime import datetime
from celery import shared_task
from django.core.mail import EmailMessage
from .models import MessageBoard
from django.template.loader import render_to_string


@shared_task(name='email_notification')
def send_email_task(subject, body, emailaddress):
        email = EmailMessage(subject, body, to=[emailaddress])
        email.send()
        return emailaddress


@shared_task(name='monthly_newsletter')
def send_monthly_newsletter():
    subject = 'Boletín Mensual'
    subscribers = MessageBoard.objects.get(id=1).subscribers.filter(
        profile__newsletter_subscribed=True
    )
    
    for subscriber in subscribers:
        body = render_to_string('a_messageboard/newsletter.html', {'name': subscriber.profile.name})
        email = EmailMessage(subject, body, to=[subscriber.email])
        email.content_subtype = 'html'
        email.send()
    
    current_month = datetime.now().strftime('%B')
    subscriber_count = subscribers.count()
    return f'{current_month} Boletín para {subscriber_count} subscriptores.'