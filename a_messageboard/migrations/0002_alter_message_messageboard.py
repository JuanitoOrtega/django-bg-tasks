# Generated by Django 5.1.2 on 2024-11-04 16:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a_messageboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='messageboard',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='a_messageboard.messageboard', verbose_name='Mensaje'),
        ),
    ]
