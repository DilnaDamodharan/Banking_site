# Generated by Django 4.2 on 2023-07-27 20:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bankapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='branch',
            old_name='branchname',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='district',
            old_name='distrctname',
            new_name='name',
        ),
    ]