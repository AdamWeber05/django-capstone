# Generated by Django 3.0.4 on 2020-11-25 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Boat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('so_num', models.CharField(max_length=10)),
                ('model', models.CharField(max_length=10)),
                ('color', models.CharField(max_length=10)),
                ('current_step', models.CharField(max_length=10)),
                ('prep', models.DateField(blank=True, null=True)),
                ('gel', models.DateField(blank=True, null=True)),
                ('skin', models.DateField(blank=True, null=True)),
                ('bulk', models.DateField(blank=True, null=True)),
                ('floor', models.DateField(blank=True, null=True)),
                ('box', models.DateField(blank=True, null=True)),
                ('pull', models.DateField(blank=True, null=True)),
                ('grind', models.DateField(blank=True, null=True)),
                ('cut', models.DateField(blank=True, null=True)),
                ('patch', models.DateField(blank=True, null=True)),
                ('hw', models.DateField(blank=True, null=True)),
                ('cap', models.DateField(blank=True, null=True)),
                ('foam', models.DateField(blank=True, null=True)),
                ('con', models.DateField(blank=True, null=True)),
                ('mtr', models.DateField(blank=True, null=True)),
                ('rig', models.DateField(blank=True, null=True)),
                ('uph', models.DateField(blank=True, null=True)),
                ('cc', models.DateField(blank=True, null=True)),
                ('insp', models.DateField(blank=True, null=True)),
            ],
        ),
    ]
