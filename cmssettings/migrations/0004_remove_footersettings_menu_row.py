# Generated by Django 5.0 on 2024-01-01 05:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        (
            "cmssettings",
            "0003_footersettings_address_footersettings_address_title_and_more",
        ),
    ]

    operations = [
        migrations.RemoveField(
            model_name="footersettings",
            name="menu_row",
        ),
    ]
