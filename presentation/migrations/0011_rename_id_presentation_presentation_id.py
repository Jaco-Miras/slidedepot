# Generated by Django 4.0.3 on 2022-04-30 08:47

from django.db import migrations


class Migration(migrations.Migration):
    atomic = False

    dependencies = [
        ('presentation', '0010_alter_presentation_file'),
    ]

    operations = [
        migrations.RenameField(
            model_name='presentation',
            old_name='id',
            new_name='presentation_id',
        ),
    ]
