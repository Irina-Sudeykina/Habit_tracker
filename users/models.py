from django.db import models
from django.contrib.auth.models import AbstractUser
from users.managers import CustomUserManager  # Импортируем наш кастомный менеджер


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='Email')

    objects = CustomUserManager()  # Используем кастомный менеджер

    phone = models.CharField(
        max_length=35, 
        verbose_name='Телефон', 
        blank=True, 
        null=True, 
        help_text='Введите номер телефона'
    )
    tg_nick = models.CharField(
        max_length=50, 
        verbose_name='Ник телеграмма', 
        blank=True, 
        null=True, 
        help_text='Введите ник телеграмма'
    )
    avatar = models.ImageField(
        upload_to='users/avatars/', 
        verbose_name='Аватар', 
        blank=True, 
        null=True, 
        help_text='Загрузите аватар'
    )
    tg_chat_id = models.CharField(
        max_length=50, 
        blank=True, 
        null=True, 
        verbose_name='Телеграм chat-id', 
        help_text='Укажите телеграм chat-id'
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.email
