# Generated by Django 3.1.3 on 2021-03-13 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solookup', '0009_remove_boat_dealer_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boat',
            name='so_num',
            field=models.CharField(max_length=10, primary_key=True, serialize=False),
        ),
    ]
