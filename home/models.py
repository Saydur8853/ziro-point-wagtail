from django.db import models
from wagtailmenus.models import MenuPage 
from wagtail.models import Page
from wagtail.fields import StreamField
from wagtail.admin.panels import FieldPanel
from . import blocks
from wagtail.models import Page
from wagtail.api import APIField
from django.utils.translation import gettext_lazy as _


class HomePage(MenuPage):
    header = StreamField(
        [
            ("banner", blocks.HeroBanner()),
        ],
        null=True,
        blank=True,
        use_json_field=True,
    )
    body = StreamField(
        [
            ("card_image_with_title", blocks.TextOverCards()),
            ("image_with_cta", blocks.ImageWithCTA()),
            ("zigzag_image_and_content", blocks.ZigzagImageAndContent()),
            ("clints_section", blocks.ClintsSection()),
           
        ],
        null=True,
        blank=True,
        use_json_field=True,
    )

    content_panels = MenuPage.content_panels + [
        FieldPanel("header"),
        FieldPanel("body"),
    ]
    api_fields = [
        APIField("header"),
        APIField("body"),
    ]
    subpage_types = ["home.BasicPage"]


"""
.########.....###.....######..####..######.
.##.....##...##.##...##....##..##..##....##
.##.....##..##...##..##........##..##......
.########..##.....##..######...##..##......
.##.....##.#########.......##..##..##......
.##.....##.##.....##.##....##..##..##....##
.########..##.....##..######..####..######.
"""

class BasicPage(MenuPage):

    body = StreamField(
        [
            ("banner_with_tile", blocks.BannerWithTile()),
            ("card_image_with_title", blocks.TextOverCards()),
            ("image_with_cta", blocks.ImageWithCTA()),
            ("title_and_icon_block", blocks.TitleAndIconBlock()),
            ("zigzag_image_and_content", blocks.ZigzagImageAndContent()),
            ("highlighted_carousel", blocks.HighlightedCarousel()),
            ("clints_section", blocks.ClintsSection()),
            ("title_with_cta_service", blocks.TitleWithCtaService()),
            ("info_card_block", blocks.InfoCardBlock()), 
            ("redirect_image_info", blocks.RedirectImageInfoBlock()), 
            
                
        ],
        blank=True, 
        null=True, 
        use_json_field=True,
    )

    
    content_panels = MenuPage.content_panels + [
        FieldPanel("body"),
    ]

    api_fields = [
        APIField("body"),
    ]
    parent_page_types = ["home.HomePage", "home.BasicPage"]
    subpage_types = ["home.BasicPage"]


#    ███    ██ ███████ ██     ██ ███████     ██      ███████ ████████ ████████ ███████ ██████
#    ████   ██ ██      ██     ██ ██          ██      ██         ██       ██    ██      ██   ██
#    ██ ██  ██ █████   ██  █  ██ ███████     ██      █████      ██       ██    █████   ██████
#    ██  ██ ██ ██      ██ ███ ██      ██     ██      ██         ██       ██    ██      ██   ██
#    ██   ████ ███████  ███ ███  ███████     ███████ ███████    ██       ██    ███████ ██   ██




class Newsletter(models.Model):
    email = models.EmailField(_("Email"), max_length=254, unique=True)
    subscribed_at = models.DateTimeField(
        _("Subscribed At"), auto_now=False, auto_now_add=True, blank=True
    )

    def __str__(self):
        return f"{self.email}"

    class Meta:
        verbose_name = "Newsletter Subscriber"