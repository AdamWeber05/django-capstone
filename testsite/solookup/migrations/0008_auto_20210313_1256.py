# Generated by Django 3.1.3 on 2021-03-13 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solookup', '0007_auto_20210313_1252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boat',
            name='dealer_name',
            field=models.CharField(blank=True, default='', max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='boat',
            name='so_num',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
