from home.blocks import CallToActionBlock
from wagtail import blocks
from wagtailutils import blocks as util_blocks


class InternalPageBlock(blocks.StructBlock):
    page = blocks.PageChooserBlock()
    override_title = blocks.CharBlock(required=False)
    open_in_new_tab = blocks.BooleanBlock(required=False)

    class Meta:
        # Translators: Navigation Menu Item Type
        verbose_name = "Internal Page Block"

    def get_serializable_data(self, obj):
        result = self.get_api_representation(obj)
        page = obj["page"]
        result["page"] = page.serializable_data()
        result["page"]["url"] = page.url
        return result


class FooterLogoBlock(blocks.StructBlock):
    image = util_blocks.ImageChooserBlock(
        required=False,
        help_text="Optimal Dimension: width-202px",
        rendition_rules={
            "original": "width-202|format-webp",
            "original_fallback": "width-202",
            "tab": "width-202|format-webp",
            "tab_fallback": "width-202",
            "mobile": "width-133|format-webp",
            "mobile_fallback": "width-133",
        },
    )
    cta = CallToActionBlock(required=False)

    class Meta:
        icon = "image"
