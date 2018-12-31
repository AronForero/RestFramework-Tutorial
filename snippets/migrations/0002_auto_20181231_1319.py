# Generated by Django 2.1.4 on 2018-12-31 13:19

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='snippet',
            name='owner',
            field=models.ForeignKey(on_delete='CASCADE', related_name='snippets', to=settings.AUTH_USER_MODEL),
        ),
    ]
