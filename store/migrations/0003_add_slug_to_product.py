# Generated by Django 5.1.6 on 2025-02-27 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0002_rename_price_to_unit_price"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="slug",
            field=models.SlugField(default="-"),
            preserve_default=False,
        ),
    ]
