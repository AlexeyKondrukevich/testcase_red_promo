# Generated by Django 4.2.2 on 2023-06-25 11:52

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("books", "0006_rename_current_reader_reservation_reader"),
    ]

    operations = [
        migrations.AlterField(
            model_name="reservation",
            name="status",
            field=models.CharField(
                choices=[("RES", "Reserved"), ("RET", "Returned")],
                default="RES",
                max_length=10,
            ),
        ),
    ]
