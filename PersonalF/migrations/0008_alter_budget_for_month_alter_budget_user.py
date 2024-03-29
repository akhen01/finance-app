# Generated by Django 4.2.6 on 2024-03-15 17:15

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('PersonalF', '0007_alter_budget_for_month'),
    ]

    operations = [
        migrations.AlterField(
            model_name='budget',
            name='for_month',
            field=models.DateField(default=datetime.datetime(2024, 3, 15, 17, 15, 23, 4346, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='budget',
            name='user',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]