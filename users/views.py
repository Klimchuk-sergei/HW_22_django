from django.contrib.auth.views import LoginView, LogoutView
from django.core.mail import send_mail
from django.views import View
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.conf import settings

from users.forms import UserRegisterForm, UserLoginForm
from users.models import User


# Create your views here.

class UserRegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        response = super().form_valid(form)
        user = form.save()
        send_mail(
            subject='Поздравляем с регистрацией',
            message='Вы успешно зарегистрировались на нашем сайте',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[user.email]
        )
        return response

class UserLoginView(LoginView):
    form_class = UserLoginForm
    template_name = 'users/login.html'

class UserLogoutView(LogoutView):
    pass
