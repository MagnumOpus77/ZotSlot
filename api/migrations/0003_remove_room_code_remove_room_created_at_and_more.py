# Generated by Django 4.0.5 on 2022-07-09 01:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_room_course_codes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='code',
        ),
        migrations.RemoveField(
            model_name='room',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='room',
            name='guest_can_pause',
        ),
        migrations.RemoveField(
            model_name='room',
            name='host',
        ),
        migrations.RemoveField(
            model_name='room',
            name='votes_to_skip',
        ),
    ]
