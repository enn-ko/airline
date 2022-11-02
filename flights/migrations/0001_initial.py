# Generated by Django 4.1.2 on 2022-10-31 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="flight",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("origin", models.CharField(max_length=64)),
                ("destination", models.CharField(max_length=64)),
                ("duration", models.IntegerField()),
            ],
        ),
    ]
