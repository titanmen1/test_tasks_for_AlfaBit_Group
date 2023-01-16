from django.db import models

from task1.utils import create_methods_from_attributes

# Мне еще нравится идея, чтобы атрибуты стейтов хранить в отдельном классе, тогда можно было бы в декоратор передавать
# любое количество стейтов и добавть методы, то по переданным стейтам
@create_methods_from_attributes
class DeliveryState(models.Model):
    class Meta:
        verbose_name = u"Состояние доставки"
        verbose_name_plural = u"Состояния доставок"

    STATE_NEW = 1  # Новая
    STATE_ISSUED = 2  # Выдана курьеру
    STATE_DELIVERED = 3  # Доставлена
    STATE_HANDED = 4  # Курьер сдал
    STATE_REFUSED = 5  # Отказ
    STATE_PAID_REFUSED = 6  # Отказ с оплатой курьеру
    STATE_COMPLETE = 7  # Завершена
    STATE_NONE = 8  # Не определено

    name = models.CharField(
        u"Название",
        max_length=50,
        unique=True,
    )

@create_methods_from_attributes
class LeadState(models.Model):
    # pk экземпляров модели

    STATE_NEW = 1  # Новый
    STATE_IN_PROGRESS = 2  # В работе
    STATE_POSTPONED = 3  # Приостановлен
    STATE_DONE = 4  # Завершен

    name = models.CharField(
        u"Название",
        max_length=50,
        unique=True,
    )

