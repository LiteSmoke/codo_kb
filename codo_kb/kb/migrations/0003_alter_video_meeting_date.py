# Generated by Django 4.0.6 on 2022-07-07 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kb', '0002_alter_video_filepath_alter_video_meeting_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='meeting_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
