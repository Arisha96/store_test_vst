# Generated by Django 3.2.12 on 2022-04-12 08:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store_test_vst', '0015_alter_property_options'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Property',
            new_name='TechProperty',
        ),
    ]