# Generated by Django 4.2.6 on 2024-03-16 17:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PersonalF', '0013_rename_user_budget_owner_rename_user_money_owner_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='money',
            old_name='name',
            new_name='discription',
        ),
        migrations.AlterField(
            model_name='budget',
            name='for_month',
            field=models.DateField(default=datetime.datetime(2024, 3, 16, 17, 55, 26, 808054, tzinfo=datetime.timezone.utc)),
        ),
    ]