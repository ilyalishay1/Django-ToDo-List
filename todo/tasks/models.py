from django.db import models


class Task(models.Model):
    title = models.CharField('Задачи', max_length=150)
    complete = models.BooleanField('Выполнено', default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Цель'
        verbose_name_plural = 'Задачи'
