# Generated by Django 4.1.5 on 2023-01-11 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loyaltycard', '0002_remove_card_pub_date_remove_card_question_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='status',
            field=models.IntegerField(choices=[(1, 'Deactivated'), (2, 'Activated'), (3, 'Expired')], default=1),
        ),
        migrations.AlterField(
            model_name='card',
            name='numb',
            field=models.PositiveIntegerField(verbose_name='Number'),
        ),
        migrations.AlterField(
            model_name='card',
            name='series',
            field=models.PositiveIntegerField(verbose_name='Series'),
        ),
    ]
