# Generated by Django 3.0.6 on 2020-05-29 13:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payroll', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='job',
            new_name='jobDesc',
        ),
    ]
