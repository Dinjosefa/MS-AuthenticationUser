# Generated by Django 3.2.7 on 2021-12-07 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_App', '0003_alter_user_is_superuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='cantlib',
            field=models.BigIntegerField(default=0, verbose_name='Cantidad_Libros'),
        ),
    ]
