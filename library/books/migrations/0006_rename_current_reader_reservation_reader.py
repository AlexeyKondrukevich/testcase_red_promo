# Generated by Django 4.2.2 on 2023-06-25 11:50

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("books", "0005_reservation"),
    ]

    operations = [
        migrations.RenameField(
            model_name="reservation",
            old_name="current_reader",
            new_name="reader",
        ),
    ]
