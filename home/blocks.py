from wagtail import blocks
from wagtailutils import blocks as util_blocks
from wagtail_color_panel.blocks import NativeColorBlock

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
class CallToActionBlock(blocks.StructBlock):
    link = util_blocks.PageOrLinkBlock(required=False)
    anchor = blocks.CharBlock(required=False)

    class Meta:
        icon = "link"


class LabeledCallToActionBlock(CallToActionBlock):
    label = blocks.CharBlock(required=False, default="Read More")

    class Meta:
        icon = "link"

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


class Banner(blocks.StructBlock):
    hero_image = util_blocks.ImageChooserBlock(
        required=True,
        help_text="Optimal Dimension : 1920x1080",
        rendition_rules={
            "original": "fill-1920x1080-c0|format-webp",
            "original_fallback": "fill-1920x1080-c0",
            "box": "fill-365x300-c0|format-webp",
            "box_fallback": "fill-365x300-c0",
        },
    )
    hero_image_for_mobile = util_blocks.ImageChooserBlock(
        required=False,
        help_text="Optimal Dimension : max width 450px",
        rendition_rules={
            "original": "width-450|scale-100|format-webp",
            "original_fallback": "width-450|scale-100",
        },
    )

class HeroBanner(blocks.StructBlock):
    banners = blocks.ListBlock(
        Banner(),
        required=False,
    )


class CardImages(blocks.StructBlock):
    image_title = util_blocks.RichTextBlock(required=False)
    title_color = NativeColorBlock(required=False)
    card_image = util_blocks.ImageChooserBlock(
        required=True,
        help_text="Optimal Dimension : width-450",
        rendition_rules={
            "original": "width-450|scale-100|format-webp",
            "original_fallback": "width-450|scale-100",
        },
    )

class TextOverCards(blocks.StructBlock):
    title = blocks.CharBlock(required=False)
    text = util_blocks.RichTextBlock(required=False)
    card_images = blocks.ListBlock(
        CardImages(),
        required=False,
    )


class ImageWithCTA(blocks.StructBlock):
    title = blocks.CharBlock(required=False)
    text = util_blocks.RichTextBlock(required=False)
    cta = LabeledCallToActionBlock()
    image1 = util_blocks.ImageChooserBlock(
        required=False,
        help_text="Optimal Dimension : max width 450px",
        rendition_rules={
            "original": "width-450|scale-100|format-webp",
            "original_fallback": "width-450|scale-100",
        },
    )
    image2 = util_blocks.ImageChooserBlock(
        required=False,
        help_text="Optimal Dimension : max width 450px",
        rendition_rules={
            "original": "width-450|scale-100|format-webp",
            "original_fallback": "width-450|scale-100",
        },
    )

class ImageWithTitleText(blocks.StructBlock):
    title = blocks.CharBlock(required=False)
    text = util_blocks.RichTextBlock(required=False)
    image = util_blocks.ImageChooserBlock(
        required=False,
        help_text="Optimal Dimension : 710x550",
        rendition_rules={
            "original": "fill-710x550-c0|format-webp",
            "original_fallback": "fill-710x550-c0",
        },
    )


class ZigzagImageAndContent(blocks.StructBlock):
    title = blocks.CharBlock(required=False)
    content = blocks.ListBlock(ImageWithTitleText(),required=False)
    


class ClintsSection(blocks.StructBlock):
    title = blocks.CharBlock(required=False)
    text = util_blocks.RichTextBlock(required=False)
    logos = blocks.ListBlock(util_blocks.ImageChooserBlock(
        required=False,
        help_text="Optimal Dimension : width-250",
        rendition_rules={
            "original": "width-250|format-webp",
            "original_fallback": "width-250",
        },
    ))




# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                          # basic block
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

class IconTiles(blocks.StructBlock):
    title = blocks.CharBlock(required=False)
    image = util_blocks.ImageChooserBlock(
        required=False,
        help_text="Optimal Dimension : width-300",
        rendition_rules={
            "original": "width-300|format-webp",
            "original_fallback": "width-300",
        },
    )

class BannerWithTile(blocks.StructBlock):
    title = util_blocks.RichTextBlock(required=False)
    subtitle = util_blocks.RichTextBlock(required=False)
    text = util_blocks.RichTextBlock(required=False)
    background_image = util_blocks.ImageChooserBlock(
        required=True,
        help_text="Optimal Dimension : 1920x1080",
        rendition_rules={
            "original": "fill-1920x1080-c0|format-webp",
            "original_fallback": "fill-1920x1080-c0",
        },
    )
    cta = LabeledCallToActionBlock()
    icon_tiles = blocks.ListBlock(IconTiles(),)
    
class IconAndTitle(blocks.StructBlock):
    icon = blocks.ListBlock(util_blocks.ImageChooserBlock(
        required=False,
        help_text="Optimal Dimension : width-300",
        rendition_rules={
            "original": "width-300|format-webp",
            "original_fallback": "width-300",
        },
    ))
    icon_hover_color_active = blocks.BooleanBlock(required=False, default=False)
    icon_hover_color =  NativeColorBlock(required=False)
    icon_title = blocks.CharBlock(required=False)


class TitleAndIconBlock(blocks.StructBlock):
    title = util_blocks.RichTextBlock(required=False)
    text = util_blocks.RichTextBlock(required=False)
    discuss_cta = LabeledCallToActionBlock(required=False)
    social_cta = LabeledCallToActionBlock(required=False)
    icons_and_title = blocks.ListBlock(IconAndTitle(),)
    
class CarouselBlock(blocks.StructBlock):
    logo = util_blocks.ImageChooserBlock(
        required=True,
        help_text="Optimal Dimension : width-300",
        rendition_rules={
            "original": "width-300|format-webp",
            "original_fallback": "width-300",
        },
    )
    rating = blocks.ChoiceBlock(choices=(("1", "1"),("2", "2"), ("3", "3"),("4", "4"),("5", "5"),), default="3")
    text = util_blocks.RichTextBlock(required=False)
    reviewer_image = util_blocks.ImageChooserBlock(
        required=True,
        help_text="Optimal Dimension : width-300",
        rendition_rules={
            "original": "width-300|format-webp",
            "original_fallback": "width-300",
        },
    )
    reviewer_name = blocks.CharBlock(required=False)
    reviewer_subtitle = util_blocks.RichTextBlock(required=False)

class HighlightedCarousel(blocks.StructBlock):
    title = util_blocks.RichTextBlock(required=False)
    subtitle = util_blocks.RichTextBlock(required=False)
    carousels = blocks.ListBlock(CarouselBlock())

class CtaCardsBlock(blocks.StructBlock):
    image = util_blocks.ImageChooserBlock(
        required=True,
        help_text="Optimal Dimension : 290x350",
        rendition_rules={
            "original": "fill-290x350-c0|format-webp",
            "original_fallback": "fill-290x350-c0",
        },
    )
    title = blocks.CharBlock(required=False)
    text = util_blocks.RichTextBlock(required=False)
    cta = LabeledCallToActionBlock(required=False)

class TitleWithCtaService(blocks.StructBlock):
    title = blocks.CharBlock(required=False)
    text = util_blocks.RichTextBlock(required=False)
    carousels = blocks.ListBlock(CtaCardsBlock())
    
class InfoCard(blocks.StructBlock):
    image = util_blocks.ImageChooserBlock(
        required=True,
        help_text="Optimal Dimension : 510x380",
        rendition_rules={
            "original": "fill-510x380-c0|format-webp",
            "original_fallback": "fill-510x380-c0",
        },
    )
    title = blocks.CharBlock(required=False)
    text = util_blocks.RichTextBlock(required=False)
    
class InfoCardBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=False)
    InfoCards = blocks.ListBlock(InfoCard())

class ImageInfo(blocks.StructBlock):
    image = util_blocks.ImageChooserBlock(
        required=True,
        help_text="Optimal Dimension : 355x500",
        rendition_rules={
            "original": "fill-355x500-c0|format-webp",
            "original_fallback": "fill-355x500-c0",
        },
    )
    title = blocks.CharBlock(required=False)
    text = util_blocks.RichTextBlock(required=False)
    cta = LabeledCallToActionBlock(required=False)
    
class RedirectImageInfoBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=False)
    ImageInfos = blocks.ListBlock(ImageInfo())