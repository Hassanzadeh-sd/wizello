# Generated by Django 2.2.7 on 2019-11-17 09:57

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0002_auto_20191116_1217'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ['deadline'], 'verbose_name': 'Task', 'verbose_name_plural': 'Tasks'},
        ),
        migrations.AlterField(
            model_name='task',
            name='assignee',
            field=models.ManyToManyField(related_name='taskassignee', to=settings.AUTH_USER_MODEL),
        ),
    ]
