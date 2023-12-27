from django.db import models

from users.models import User

NULLABLE = {'blank': True, 'null': True}


class Habit(models.Model):

    user = models.ForeignKey(User, verbose_name="пользователь", on_delete=models.CASCADE, **NULLABLE)
    place = models.CharField(max_length=100, verbose_name='место')
    time = models.TimeField(verbose_name="время")
    action = models.CharField(max_length=300, verbose_name="действие")
    is_pleasant = models.BooleanField(verbose_name="приятная привычка", default=False)
    bound_habit = models.ForeignKey("self", on_delete=models.SET_NULL, verbose_name="связанная привычка", **NULLABLE)
    periodicity = models.PositiveIntegerField(verbose_name="Периодичность в днях", default=1)
    reward = models.CharField(max_length=400, verbose_name="Вознаграждение", **NULLABLE)
    duration = models.PositiveIntegerField(verbose_name="Время на выполнение")
    is_public = models.BooleanField(default=False, verbose_name="видна всем")

    def __str__(self):
        return f"я буду {self.action} в {self.time} в {self.place}"

    class Meta:
        verbose_name = "привычка"
        verbose_name_plural = "привычки"
