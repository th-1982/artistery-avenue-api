# Generated by Django 3.2.23 on 2024-02-19 22:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contact',
            options={},
        ),
        migrations.RemoveField(
            model_name='contact',
            name='content',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='reason',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='updated_at',
        ),
        migrations.AddField(
            model_name='contact',
            name='email',
            field=models.CharField(default=1, max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contact',
            name='message',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contact',
            name='name',
            field=models.CharField(default=django.utils.timezone.now, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contact',
            name='subject',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]