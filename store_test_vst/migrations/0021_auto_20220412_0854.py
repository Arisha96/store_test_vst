# Generated by Django 3.2.12 on 2022-04-12 08:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store_test_vst', '0020_alter_property_options'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Property',
            new_name='Characteristic',
        ),
        migrations.AlterModelOptions(
            name='characteristic',
            options={'default_related_name': 'characteristic'},
        ),
    ]
