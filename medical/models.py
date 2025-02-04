from django.db import models

from users.models import MakeAnAppointment

NULLABLE = {
    'blank': True,
    'null': True
}


class Medical(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name='Название услуги'
    )
    information = models.TextField(
        verbose_name='Описание услуги',
        **NULLABLE
    )
    price = models.PositiveIntegerField(
        verbose_name='Стоимость услуги'
    )
    subscription_to_service = models.ForeignKey(
        MakeAnAppointment,
        on_delete=models.CASCADE,
        verbose_name='Запись на услугу',
        **NULLABLE
    )
    photo = models.ImageField(
        upload_to='media/medical/',
        verbose_name='Аватар специалиста',
        **NULLABLE
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Медицинская услуга'
        verbose_name_plural = 'Медицинские услуги'
