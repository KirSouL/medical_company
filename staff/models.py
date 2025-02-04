from django.db import models

NULLABLE = {
    'blank': True,
    'null': True
}


class StaffMedical(models.Model):
    first_name = models.CharField(
        max_length=150,
        verbose_name='Имя специалиста',
        help_text='Введите имя сотрудника'
    )
    patronymic = models.CharField(
        max_length=150,
        verbose_name='Отчество специалиста',
        help_text='Введите отчество сотрудника'
    )
    last_name = models.CharField(
        max_length=150,
        verbose_name='Фамилия специалиста',
        help_text='Введите фамилию сотрудника'
    )
    position = models.CharField(
        max_length=150,
        verbose_name='Должность специалиста',
        help_text='Введите должость сотрудника'
    )
    about_employee = models.TextField(
        verbose_name='Информация о специалисте',
        help_text='Укажите специализацию и навыки',
        **NULLABLE
    )
    avatar = models.ImageField(
        upload_to='media/staff/',
        verbose_name='Аватар специалиста',
        **NULLABLE
    )
    experience = models.PositiveIntegerField(
        verbose_name='Стаж специалиста',
        **NULLABLE
    )

    def __str__(self):
        return f'Имя: {self.first_name}, Отчество: {self.patronymic}, Фамилия: {self.last_name}'

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'
