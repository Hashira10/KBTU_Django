# Generated by Django 4.1.7 on 2024-04-07 10:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0005_user_consent_to_emails'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='is_free',
        ),
        migrations.RemoveField(
            model_name='book',
            name='notify_on_addition',
        ),
        migrations.RemoveField(
            model_name='book',
            name='price',
        ),
        migrations.RemoveField(
            model_name='user',
            name='consent_to_emails',
        ),
    ]
