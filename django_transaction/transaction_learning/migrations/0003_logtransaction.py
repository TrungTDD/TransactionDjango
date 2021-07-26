# Generated by Django 3.2.5 on 2021-07-26 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transaction_learning', '0002_rename_user_account'),
    ]

    operations = [
        migrations.CreateModel(
            name='LogTransaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_created=True)),
                ('acount', models.CharField(max_length=256)),
                ('transaction_type', models.CharField(max_length=10)),
                ('status', models.CharField(max_length=10)),
            ],
        ),
    ]
