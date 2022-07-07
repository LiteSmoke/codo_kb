# Generated by Django 4.0.6 on 2022-07-07 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kb', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='filepath',
            field=models.CharField(blank=True, max_length=512),
        ),
        migrations.AlterField(
            model_name='video',
            name='meeting_date',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='video',
            name='meeting_name',
            field=models.CharField(blank=True, max_length=512),
        ),
        migrations.AlterField(
            model_name='video',
            name='participants',
            field=models.CharField(blank=True, max_length=512),
        ),
        migrations.AlterField(
            model_name='video',
            name='tags',
            field=models.ManyToManyField(blank=True, to='kb.tag'),
        ),
    ]