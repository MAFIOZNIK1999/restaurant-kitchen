# Generated by Django 5.0.3 on 2024-03-19 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("kitchen", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cook",
            name="years_of_experience",
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
