# Generated by Django 5.1.1 on 2024-09-15 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("restaurant", "0003_rename_capacity_table_seats"),
    ]

    operations = [
        migrations.AddField(
            model_name="booking",
            name="message",
            field=models.TextField(blank=True, null=True, verbose_name="Сообщение"),
        ),
    ]
