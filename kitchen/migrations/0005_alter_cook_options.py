# Generated by Django 5.0.3 on 2024-03-19 18:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("kitchen", "0004_alter_cook_options"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="cook",
            options={"verbose_name": "cooks", "verbose_name_plural": "cooks"},
        ),
    ]
