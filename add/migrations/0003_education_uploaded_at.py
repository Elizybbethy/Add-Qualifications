# Generated by Django 3.0.8 on 2023-10-20 19:43

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('add', '0002_auto_20231020_1853'),
    ]

    operations = [
        migrations.AddField(
            model_name='education',
            name='uploaded_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]