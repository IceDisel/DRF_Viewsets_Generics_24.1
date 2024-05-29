from django.contrib.auth.models import AbstractUser
from django.db import models

from lessons.models import Course, Lesson

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True, verbose_name='почта')
    phone = models.CharField(max_length=35, unique=True, verbose_name='телефон', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='аватар', **NULLABLE)
    city = models.CharField(max_length=20, verbose_name='город проживания', **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Payment(models.Model):
    METHOD_CHOICES = [('transfer', 'Перевод на счет'), ('cash', 'Наличные'), ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь', **NULLABLE)
    pay_date = models.DateField(verbose_name='Дата оплаты')
    pay_course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Оплаченный курс', **NULLABLE)
    pay_lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name='Оплаченный урок', **NULLABLE)
    money = models.IntegerField(verbose_name='Оплаченная сумма')
    pay_method = models.CharField(choices=METHOD_CHOICES, default=METHOD_CHOICES[0], verbose_name='Способ оплаты')

    def __str__(self):
        return f'{self.user} - {self.money}'

    class Meta:
        verbose_name = 'Оплата'
        verbose_name_plural = 'Оплата'
