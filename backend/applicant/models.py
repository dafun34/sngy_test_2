from django.db import models
#
# Имя: name (varchar 200)
# Компания: company_name (varchar 100)
# Должность: position_name (varchar 100)
# Дата приёма: hire_date (date)
# Дата увольнения: fire_date (date, null)
# Ставка, руб.: salary (int)
# Ставка, %: fraction (int)
# База, руб.: base (int)
# Аванс, руб.: advance (int)
# Почасовая оплата: by_hours (boolean)


class Occupation(models.Model):
    name = models.CharField(max_length=200, verbose_name='Имя')
    company_name = models.CharField(max_length=100, verbose_name='Компания')
    position_name = models.CharField(max_length=100, verbose_name='Должность')
    hire_date = models.DateField(verbose_name='Дата приёма')
    fire_date = models.DateField(null=True,
                                 verbose_name='Дата увольнения',
                                 blank=True)
    salary = models.PositiveIntegerField(verbose_name='Ставка, руб')
    fraction = models.PositiveSmallIntegerField(verbose_name='Ставка, %')
    base = models.PositiveIntegerField(verbose_name='База, руб')
    advance = models.PositiveIntegerField(verbose_name='Аванс, руб')
    by_hours = models.BooleanField(verbose_name='Почасовая оплата')

    def __str__(self):
        return self.name

