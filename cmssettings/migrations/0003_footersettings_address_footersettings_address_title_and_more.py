# Generated by Django 5.0 on 2024-01-01 05:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cmssettings", "0002_remove_footersettings_logos_and_more"),
        ("wagtailmenus", "0023_remove_use_specific"),
    ]

    operations = [
        migrations.AddField(
            model_name="footersettings",
            name="address",
            field=models.CharField(
                blank=True, max_length=200, null=True, verbose_name="Address"
            ),
        ),
        migrations.AddField(
            model_name="footersettings",
            name="address_title",
            field=models.CharField(
                blank=True,
                default="Contact Us",
                max_length=200,
                null=True,
                verbose_name="Address title",
            ),
        ),
        migrations.AddField(
            model_name="footersettings",
            name="menu_column_3",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="wagtailmenus.flatmenu",
                verbose_name="Menu Column 3",
            ),
        ),
        migrations.AddField(
            model_name="footersettings",
            name="menu_title_3",
            field=models.CharField(
                blank=True, max_length=200, null=True, verbose_name="Menu Title 3"
            ),
        ),
        migrations.AddField(
            model_name="footersettings",
            name="phone_number",
            field=models.CharField(
                blank=True, max_length=200, null=True, verbose_name="Phone Number"
            ),
        ),
        migrations.AddField(
            model_name="footersettings",
            name="website",
            field=models.CharField(
                blank=True, max_length=200, null=True, verbose_name="Website"
            ),
        ),
    ]
