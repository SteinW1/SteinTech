# Generated by Django 3.2.4 on 2022-04-16 22:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0003_auto_20220416_1424'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ingredient',
            old_name='amount',
            new_name='quantity',
        ),
    ]