# Generated by Django 2.2.7 on 2019-11-20 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('request', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='position',
            field=models.CharField(choices=[('M', 'Manager'), ('EO', 'Employee Organization')], default='EO', max_length=15),
        ),
    ]
