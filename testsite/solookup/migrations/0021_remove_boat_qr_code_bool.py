# Generated by Django 3.1.3 on 2021-04-04 12:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('solookup', '0020_boat_qr_code_bool'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='boat',
            name='qr_code_bool',
        ),
    ]
