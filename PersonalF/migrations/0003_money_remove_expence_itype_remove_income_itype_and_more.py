# Generated by Django 4.2.6 on 2024-03-06 18:23

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('PersonalF', '0002_expence'),
    ]

    operations = [
        migrations.CreateModel(
            name='Money',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('type', models.CharField(choices=[('income', 'income'), ('expence', 'expence')], max_length=50)),
                ('catagory_name', models.CharField(blank=True, choices=[('Fun', 'Fun'), ('Apparel', 'Apparel'), ('Grocery', 'Grocery'), ('Cleaning', 'Cleaning'), ('Electronics', 'Electronics'), ('Furniture', 'Furniture'), ('Rent', 'Rent'), ('Bills', 'Bills')], default='Rent', max_length=50, null=True)),
                ('amount', models.IntegerField()),
                ('date', models.DateField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='expence',
            name='Itype',
        ),
        migrations.RemoveField(
            model_name='income',
            name='Itype',
        ),
        migrations.RemoveField(
            model_name='budget',
            name='Itype',
        ),
        migrations.AddField(
            model_name='budget',
            name='budget_type',
            field=models.CharField(choices=[('Fun', 'Fun'), ('Apparel', 'Apparel'), ('Grocery', 'Grocery'), ('Cleaning', 'Cleaning'), ('Electronics', 'Electronics'), ('Furniture', 'Furniture'), ('Rent', 'Rent'), ('Bills', 'Bills')], default='Rent', max_length=50),
        ),
        migrations.AddField(
            model_name='budget',
            name='for_month',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 6, 18, 23, 25, 347705, tzinfo=datetime.timezone.utc)),
        ),
        migrations.DeleteModel(
            name='budgettype',
        ),
        migrations.DeleteModel(
            name='expence',
        ),
        migrations.DeleteModel(
            name='income',
        ),
        migrations.DeleteModel(
            name='incometype',
        ),
    ]
