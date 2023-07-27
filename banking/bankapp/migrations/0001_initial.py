# Generated by Django 4.2 on 2023-07-27 19:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='district',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('distrctname', models.CharField(max_length=100)),
                ('wikilink', models.URLField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='branch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branchname', models.CharField(max_length=100)),
                ('distid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bankapp.district')),
            ],
        ),
    ]