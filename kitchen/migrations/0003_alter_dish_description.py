# Generated by Django 5.0.3 on 2024-03-19 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("kitchen", "0002_alter_cook_years_of_experience"),
    ]

    operations = [
        migrations.AlterField(
            model_name="dish",
            name="description",
            field=models.TextField(blank=True, null=True),
        ),
    ]
