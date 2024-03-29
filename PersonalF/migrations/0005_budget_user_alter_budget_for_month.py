# Generated by Django 4.2.6 on 2024-03-15 17:05

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('PersonalF', '0004_alter_budget_for_month'),
    ]

    operations = [
        migrations.AddField(
            model_name='budget',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='budget',
            name='for_month',
            field=models.DateField(default=datetime.datetime(2024, 3, 15, 17, 5, 24, 363456, tzinfo=datetime.timezone.utc)),
        ),
    ]