# Generated by Django 5.0.3 on 2024-03-16 08:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bookstore", "0002_authormodel"),
    ]

    operations = [
        migrations.AlterField(
            model_name="bookmodel",
            name="author",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="books",
                to="bookstore.authormodel",
            ),
        ),
    ]
