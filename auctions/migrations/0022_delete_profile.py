# Generated by Django 3.2 on 2021-05-18 13:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0021_alter_profile_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Profile',
        ),
    ]