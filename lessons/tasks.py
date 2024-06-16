from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings

from lessons.models import Subscription


@shared_task
def send_course_update_email(course_id):
    print('start')
    subscriptions = Subscription.objects.filter(course_id=course_id)
    emails = [subscription.user.email for subscription in subscriptions]
    send_mail(
        subject="Уведомление об обновлении курса!",
        message=f"Курс обновлен. Ознакомьтесь с новыми материалами!",
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=emails,
        fail_silently=False,
    )
