from django.db import models
from django.utils.translation import gettext_lazy as _


class Card(models.Model):  # карта
    series = models.PositiveIntegerField('Series')
    numb = models.PositiveIntegerField('Number')
    start_date = models.DateTimeField('start activate date')
    stop_date = models.DateTimeField('stop activate date')

    class Status(models.IntegerChoices):
        DEACTIVATED = 1
        ACTIVATED = 2
        EXPIRED = 3

    status = models.IntegerField(choices=Status.choices, default=1)

    def __str__(self):
        return str(self.series) + ' ' + str(self.numb)


class Purchase(models.Model):  # Покупка
    purchase = models.ForeignKey(Card, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    money = models.FloatField(default=0)

    def __str__(self):
        return self.choice_text
