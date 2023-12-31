# Generated by Django 3.0.8 on 2023-10-20 18:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('add', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='education',
            old_name='major',
            new_name='activities_and_societies',
        ),
        migrations.RenameField(
            model_name='education',
            old_name='school',
            new_name='field_of_study',
        ),
        migrations.RemoveField(
            model_name='education',
            name='end_date',
        ),
        migrations.RemoveField(
            model_name='education',
            name='start_date',
        ),
        migrations.AddField(
            model_name='education',
            name='description',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='education',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='documents/'),
        ),
        migrations.AddField(
            model_name='education',
            name='grade',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='education',
            name='school_name',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]
