from django.db import models
from django.utils.translation import gettext_lazy as _
from wagtail.admin.panels import FieldPanel, MultiFieldPanel
from wagtail.contrib.settings.models import BaseSiteSetting, register_setting
from wagtail.fields import StreamField
from wagtail.images import get_image_model_string

from .blocks import FooterLogoBlock

IMAGE_MODEL = get_image_model_string()


@register_setting
class FooterSettings(BaseSiteSetting):
    menu_title_1 = models.CharField(
        _("Menu Title 1"),
        max_length=200,
        null=True,
        blank=True,
    )
    menu_column_1 = models.ForeignKey(
        "wagtailmenus.FlatMenu",
        verbose_name=_("Menu Column 1"),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    menu_title_2 = models.CharField(
        _("Menu Title 2"),
        max_length=200,
        null=True,
        blank=True,
    )
    menu_column_2 = models.ForeignKey(
        "wagtailmenus.FlatMenu",
        verbose_name=_("Menu Column 2"),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    menu_title_3 = models.CharField(
        _("Menu Title 3"),
        max_length=200,
        null=True,
        blank=True,
    )
    menu_column_3 = models.ForeignKey(
        "wagtailmenus.FlatMenu",
        verbose_name=_("Menu Column 3"),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    address_title =  models.CharField(
        _("Address title"),
        max_length=200,
        default="Contact Us",
        null=True,
        blank=True,
    )
    address =  models.CharField(
        _("Address"),
        max_length=200,
        null=True,
        blank=True,
    )
    phone_number =  models.CharField(
        _("Phone Number"),
        max_length=200,
        null=True,
        blank=True,
    )
    website =  models.CharField(
        _("Website"),
        max_length=200,
        null=True,
        blank=True,
    )


    social_links_title = models.CharField(
        _("Social Links Title"),
        max_length=200,
        default="Socials",
        null=True,
        blank=True,
    )
    facebook = models.URLField(_("Facebook"), max_length=255, blank=True)
    instagram = models.URLField(_("Instagram "), max_length=255, blank=True)
    twitter = models.URLField(_("Twitter"), max_length=255, blank=True)
    pinterest = models.URLField(_("Pinterest"), max_length=255, blank=True)
    linked_in = models.URLField(_("LinkedIn"), max_length=255, blank=True)
    youtube = models.URLField(_("Youtube"), max_length=255, blank=True)
    email = models.EmailField(_("Email"), max_length=255, blank=True)


    copyright_line = models.CharField(
        _("copyright"),
        max_length=255,
        blank=True,
        default="© 2024 ZERO POINT. Powered By Creative Concept",
    )

    panels = [

        MultiFieldPanel(
            [
                FieldPanel("address_title"),
                FieldPanel("address"),
                FieldPanel("phone_number"),
                FieldPanel("website"),
            ],
            heading="Contact Us",
        ),

        MultiFieldPanel(
            [
                FieldPanel("social_links_title"),
                FieldPanel("facebook"),
                FieldPanel("instagram"),
                FieldPanel("twitter"),
                FieldPanel("pinterest"),
                FieldPanel("linked_in"),
                FieldPanel("youtube"),
                FieldPanel("email"),
            ],
            heading="Social Links",
        ),
        
        MultiFieldPanel(
            [
                FieldPanel("menu_title_1"),
                FieldPanel("menu_column_1"),
                FieldPanel("menu_title_2"),
                FieldPanel("menu_column_2"),
                FieldPanel("menu_title_3"),
                FieldPanel("menu_column_3"),
            ],
            heading="Menus",
        ),
        
        FieldPanel("copyright_line"),
    ]

    class Meta:
        verbose_name = "Footer Settings"


@register_setting
class GlobalSettings(BaseSiteSetting):
    opengraph_image = models.ForeignKey(
        IMAGE_MODEL,
        verbose_name=_("OpenGraph Image"),
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    google_map_key = models.CharField(
        _("Google Map API Key"), max_length=250, blank=True, null=True
    )
    google_analytic_tag = models.CharField(
        _("Google Tag for Analytic"), max_length=50, blank=True, null=True
    )
    
    panels = [
        FieldPanel("opengraph_image"),
        FieldPanel("google_map_key"),
        FieldPanel("google_analytic_tag"),
    ]

    class Meta:
        verbose_name = "Global Settings"
