# Generated by Django 4.2.7 on 2023-12-02 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habit',
            name='periodicity',
            field=models.PositiveIntegerField(default=1, verbose_name='Периодичность в днях'),
        ),
    ]