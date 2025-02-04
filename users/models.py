from django.db import models
from django.contrib.auth.models import AbstractUser

from staff.models import StaffMedical

NULLABLE = {
    'blank': True,
    'null': True
}


class User(AbstractUser):
    username = None

    email = models.EmailField(
        unique=True,
        verbose_name='Почта пользователя',
        help_text='Укажите почту в формате, к примеру: user@mail.ru',
    )
    first_name = models.CharField(
        max_length=150,
        verbose_name='Имя пользователя',
        help_text='Укажите имя'
    )
    last_name = models.CharField(
        max_length=150,
        verbose_name='Фамилия пользователя',
        help_text='Укажите фамилию'
    )
    birthday = models.DateField(
        auto_now=False,
        verbose_name='Дата рождения пользователя',
        help_text='Укажите дату рождения',
        **NULLABLE
    )
    phone = models.CharField(
        max_length=30,
        verbose_name='Телефон пользователя',
        help_text='Укажите телефон',
        **NULLABLE,
    )
    avatar = models.ImageField(
        upload_to='media/users/',
        verbose_name='Аватар пользователя',
        **NULLABLE
    )
    token = models.CharField(
        max_length=200,
        verbose_name='token',
        **NULLABLE
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'Почта пользователя: {self.email}'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class MakeAnAppointment(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Пациент',
        **NULLABLE
    )
    my_doctor = models.OneToOneField(
        StaffMedical,
        on_delete=models.SET_NULL,
        verbose_name='Врач по направлению диагностики',
        **NULLABLE
    )
    reception_date = models.DateField(
        auto_now=False,
        verbose_name='Дата записи на прием',
        **NULLABLE
    )
    created_date = models.DateField(
        auto_now_add=True,
        verbose_name='Дата создания записи'
    )
    first_name = models.CharField(
        max_length=150,
        verbose_name='Имя пациента',
        **NULLABLE
    )
    last_name = models.CharField(
        max_length=150,
        verbose_name='Фамилия пациента',
        **NULLABLE
    )
    phone_number = models.CharField(
        max_length=30,
        verbose_name='Телефон пациента',
        help_text='Укажите телефон',
        **NULLABLE,
    )
    birthday = models.DateField(
        auto_now=False,
        verbose_name='Дата рождения пациента',
        help_text='Укажите дату рождения',
        **NULLABLE
    )
    place = models.CharField(
        max_length=150,
        verbose_name='Адрес расположения клиники',
        **NULLABLE
    )

    def __str__(self):
        return f'Имя пациента: {self.first_name}, Фамилия пациента: {self.last_name}'

    class Meta:
        verbose_name = 'Запись на прием'
        verbose_name_plural = 'Записи на прием'
