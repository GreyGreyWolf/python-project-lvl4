# Generated by Django 3.1.1 on 2020-10-02 08:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Users',
            new_name='Members',
        ),
    ]