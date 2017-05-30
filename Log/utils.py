from django.core.mail import send_mail
from django.template import loader
from django.conf import settings
from celery import shared_task

@shared_task
def send_confirme_mail():
    html_content = loader.render_to_string('Log/mail.html')
    return send_mail(subject='感谢您注册Google',
              message="",
              from_email=settings.EMAIL_HOST_USER,
              recipient_list=['1484941333@qq.com'],
              fail_silently=False,
            html_message=html_content)