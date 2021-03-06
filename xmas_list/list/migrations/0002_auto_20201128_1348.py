# Generated by Django 3.1.3 on 2020-11-28 18:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('list', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gift',
            name='gift_claimed_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='gift',
            name='gift_link',
            field=models.URLField(blank=True, null=True),
        ),
    ]
