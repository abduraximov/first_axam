# Generated by Django 4.2.4 on 2023-08-16 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("second", "0002_company_discount"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="company",
            name="discount",
        ),
        migrations.AddField(
            model_name="product",
            name="discount",
            field=models.IntegerField(blank=True, max_length=100, null=True),
        ),
    ]
