# Generated by Django 2.2.24 on 2022-11-13 17:06

from django.db import migrations


def move_owner_data(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Owner = apps.get_model('property', 'Owner')
    flat_set = Flat.objects.all()
    for flat in flat_set.iterator(chunk_size=2000):
        Owner.objects.get_or_create(
            owner=flat.owner,
            owners_phonenumber=flat.owners_phonenumber,
            owner_pure_phone=flat.owner_pure_phone)


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0013_auto_20221113_2005'),
    ]

    operations = [
        migrations.RunPython(move_owner_data)
    ]
