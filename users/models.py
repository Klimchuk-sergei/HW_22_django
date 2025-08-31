from django.contrib.auth.models import AbstractUser
from django.db import models
from .managers import UserManager

# Create your models here.

class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='email')
    phone_number = models.CharField(max_length=35, verbose_name='phone number', blank=True, null=True, help_text="Введите номер телефона")
    country = models.CharField(max_length= 50, verbose_name= "country", blank=True, null=True, help_text="Введите вашу страну")
    avatar = models.ImageField(upload_to='users_avatars/', verbose_name='avatar', blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def __str__(self):
        return self.email
