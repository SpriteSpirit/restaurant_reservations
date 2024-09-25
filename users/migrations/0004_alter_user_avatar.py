# Generated by Django 5.1.1 on 2024-09-25 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0003_user_avatar"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="avatar",
            field=models.ImageField(
                blank=True,
                default="/media/users/avatars/default.jpg",
                null=True,
                upload_to="users/avatars",
                verbose_name="Фото",
            ),
        ),
    ]
