# Generated by Django 5.0 on 2023-12-27 08:11

import wagtail.blocks
import wagtail.fields
import wagtail_color_panel.blocks
import wagtailutils.blocks
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0010_alter_homepage_body"),
    ]

    operations = [
        migrations.AlterField(
            model_name="homepage",
            name="body",
            field=wagtail.fields.StreamField(
                [
                    (
                        "card_image_with_title",
                        wagtail.blocks.StructBlock(
                            [
                                ("title", wagtail.blocks.CharBlock(required=False)),
                                (
                                    "text",
                                    wagtailutils.blocks.RichTextBlock(required=False),
                                ),
                                (
                                    "card_images",
                                    wagtail.blocks.ListBlock(
                                        wagtail.blocks.StructBlock(
                                            [
                                                (
                                                    "image_title",
                                                    wagtailutils.blocks.RichTextBlock(
                                                        required=False
                                                    ),
                                                ),
                                                (
                                                    "title_color",
                                                    wagtail_color_panel.blocks.NativeColorBlock(
                                                        required=False
                                                    ),
                                                ),
                                                (
                                                    "card_image",
                                                    wagtailutils.blocks.ImageChooserBlock(
                                                        help_text="Optimal Dimension : 800x450",
                                                        rendition_rules={
                                                            "original": "fill-800x450-c0|format-webp",
                                                            "original_fallback": "fill-800x450-c0",
                                                        },
                                                        required=True,
                                                    ),
                                                ),
                                            ]
                                        ),
                                        help_text="Max image = 4",
                                        max_num=4,
                                        required=False,
                                    ),
                                ),
                            ]
                        ),
                    ),
                    (
                        "two_image_with_cta",
                        wagtail.blocks.StructBlock(
                            [
                                ("title", wagtail.blocks.CharBlock(required=False)),
                                (
                                    "text",
                                    wagtailutils.blocks.RichTextBlock(required=False),
                                ),
                                (
                                    "cta",
                                    wagtail.blocks.StructBlock(
                                        [
                                            (
                                                "link",
                                                wagtail.blocks.StreamBlock(
                                                    [
                                                        (
                                                            "page",
                                                            wagtailutils.blocks.PageChooserBlock(
                                                                max_num=1
                                                            ),
                                                        ),
                                                        (
                                                            "link",
                                                            wagtail.blocks.URLBlock(
                                                                max_num=1
                                                            ),
                                                        ),
                                                    ],
                                                    required=False,
                                                ),
                                            ),
                                            (
                                                "anchor",
                                                wagtail.blocks.CharBlock(
                                                    required=False
                                                ),
                                            ),
                                            (
                                                "label",
                                                wagtail.blocks.CharBlock(
                                                    default="Read More", required=False
                                                ),
                                            ),
                                        ]
                                    ),
                                ),
                                (
                                    "image1",
                                    wagtailutils.blocks.ImageChooserBlock(
                                        help_text="Optimal Dimension : 800x450",
                                        rendition_rules={
                                            "original": "fill-800x450-c0|format-webp",
                                            "original_fallback": "fill-800x450-c0",
                                        },
                                        required=False,
                                    ),
                                ),
                                (
                                    "image2",
                                    wagtailutils.blocks.ImageChooserBlock(
                                        help_text="Optimal Dimension : 800x450",
                                        rendition_rules={
                                            "original": "fill-800x450-c0|format-webp",
                                            "original_fallback": "fill-800x450-c0",
                                        },
                                        required=False,
                                    ),
                                ),
                            ]
                        ),
                    ),
                    (
                        "zigzag_image_and_content",
                        wagtail.blocks.StructBlock(
                            [
                                ("title", wagtail.blocks.CharBlock(required=False)),
                                (
                                    "content",
                                    wagtail.blocks.ListBlock(
                                        wagtail.blocks.StructBlock(
                                            [
                                                (
                                                    "title",
                                                    wagtail.blocks.CharBlock(
                                                        required=False
                                                    ),
                                                ),
                                                (
                                                    "text",
                                                    wagtailutils.blocks.RichTextBlock(
                                                        required=False
                                                    ),
                                                ),
                                                (
                                                    "image",
                                                    wagtailutils.blocks.ImageChooserBlock(
                                                        help_text="Optimal Dimension : 800x450",
                                                        rendition_rules={
                                                            "original": "fill-800x450-c0|format-webp",
                                                            "original_fallback": "fill-800x450-c0",
                                                        },
                                                        required=False,
                                                    ),
                                                ),
                                            ]
                                        ),
                                        required=False,
                                    ),
                                ),
                            ]
                        ),
                    ),
                    (
                        "clints_section",
                        wagtail.blocks.StructBlock(
                            [
                                ("title", wagtail.blocks.CharBlock(required=False)),
                                (
                                    "text",
                                    wagtailutils.blocks.RichTextBlock(required=False),
                                ),
                                (
                                    "logos",
                                    wagtail.blocks.ListBlock(
                                        wagtailutils.blocks.ImageChooserBlock(
                                            help_text="Optimal Dimension : width-300",
                                            rendition_rules={
                                                "original": "width-300|format-webp",
                                                "original_fallback": "width-300",
                                            },
                                            required=False,
                                        )
                                    ),
                                ),
                            ]
                        ),
                    ),
                ],
                blank=True,
                null=True,
                use_json_field=True,
            ),
        ),
    ]
