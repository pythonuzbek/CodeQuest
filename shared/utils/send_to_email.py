# from celery import shared_task
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from root.settings import EMAIL_HOST_USER
from users.models import User
from users.utils.token import account_activation_token
# from celery import shared_task


def send_email(request, email, type_):
    user = get_object_or_404(User, email=email)
    subject = 'Activate your account'
    current_site = get_current_site(request)
    from_email = EMAIL_HOST_USER
    recipient_list = [email]
    if type_ == 'register':
        message = render_to_string('auth/activate-account-for-register.html', {
            'user': user,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(str(user.pk))),
            'token': account_activation_token.make_token(user)
        })
        result = send_mail(subject, message, from_email, recipient_list)
        print('Send To Mail')
    else:
        message = render_to_string('auth/activate-account-for-forgot-password.html', {
            'user': user,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(str(user.pk))),
            'token': account_activation_token.make_token(user)
        })
        result = send_mail(subject, message, from_email, recipient_list)
        print('Send To Restet Mail')


# @shared_task
# def calculate(x, y):
#     print(x + y)
