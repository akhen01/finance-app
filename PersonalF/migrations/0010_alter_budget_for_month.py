# Generated by Django 4.2.6 on 2024-03-15 17:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PersonalF', '0009_remove_budget_user_alter_budget_for_month'),
    ]

    operations = [
        migrations.AlterField(
            model_name='budget',
            name='for_month',
            field=models.DateField(default=datetime.datetime(2024, 3, 15, 17, 17, 57, 203635, tzinfo=datetime.timezone.utc)),
        ),
    ]
