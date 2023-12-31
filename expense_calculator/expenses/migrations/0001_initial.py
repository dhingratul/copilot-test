# Generated by Django 4.1 on 2023-06-26 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('category', models.CharField(choices=[('ONLINE_SERVICES', 'ONLINE_SERVICES'), ('TRAVEL', 'TRAVEL'), ('FOOD', 'FOOD'), ('OTHER', 'OTHER')], max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
