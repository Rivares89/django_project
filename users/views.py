import random

from django.conf import settings
from django.contrib.auth.views import LoginView
from django.contrib.sites.shortcuts import get_current_site
from django.core.exceptions import ValidationError
from django.core.mail import send_mail, EmailMessage
from django.shortcuts import redirect
from django.template.loader import render_to_string
from django.urls import reverse_lazy, reverse
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.views import View
from django.views.generic import CreateView, UpdateView
from users.forms import UserProfileForm, AuthenticationForm, UserRegisterForm
from users.models import User
from django.contrib.auth.tokens import default_token_generator as token_generator


class MyLoginView(LoginView):
    form_class = AuthenticationForm

class EmailVerify(View):
    def get(self, request, uidb64, token):
        user = self.get_user(uidb64)
        if user is not None and token_generator.check_token(user, token):
            user.email_verify = True
            user.is_active = True
            user.save()
            return redirect('users:valid_verify')
        return redirect('users:invalid_verify')

    @staticmethod
    def get_user(uidb64) -> User | None:
        try:
            uid = urlsafe_base64_decode(uidb64).decode()
            user = User.objects.get(pk=uid)
        except (
                TypeError,
                ValueError,
                OverflowError,
                User.DoesNotExist,
                ValidationError,
        ):
            user = None
        return user


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')

    def form_valid(self, form: UserRegisterForm):
        user = form.save(commit=False)
        user.is_active = False
        user.save()

        self._send_confirmation_email(user)

        return redirect('users:confirm_email')

    def _send_confirmation_email(self, user: User) -> None:
        current_site = get_current_site(self.request)
        mail_subject = 'Подтвердите вашу учетную запись'
        message = render_to_string('users/acc_activate_email.html', {
            'user': user,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': token_generator.make_token(user),
        })

        email = EmailMessage(mail_subject, message, to=[user.email])
        email.send()

class ProfileView(UpdateView):
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user

def generate_new_password(request):
    new_password = User.objects.make_random_password()
    send_mail(
        subject='Вы сменили пароль',
        message=f'Ваш новый пароль: {new_password}',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[request.user.email]
    )
    request.user.set_password(new_password)
    request.user.save()

    return redirect(reverse('catalog:list'))
