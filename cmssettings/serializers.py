from rest_framework import serializers
from wagtail.api.v2.serializers import StreamField
from wagtail.models import Site
from wagtailmenus.models import MainMenu
from wagtailutils.fields import ImageRenditionField
from wagtailutils.serializers import FlatMenuItemSerializer, MainMenuItemSerializer

from .models import FooterSettings, GlobalSettings


class FooterSettingsSerializer(serializers.ModelSerializer):
    menu_column_1 = serializers.SerializerMethodField()
    menu_column_2 = serializers.SerializerMethodField()
    menu_column_3 = serializers.SerializerMethodField()


    def get_menu_column_1(self, model):
        if model.menu_column_1:
            return FlatMenuItemSerializer(
                model.menu_column_1.menu_items.all(),
                many=True,
                read_only=True,
                context=self.context,
            ).data
        else:
            return []

    def get_menu_column_2(self, model):
        if model.menu_column_2:
            return FlatMenuItemSerializer(
                model.menu_column_2.menu_items.all(),
                many=True,
                read_only=True,
                context=self.context,
            ).data
        else:
            return []
    def get_menu_column_3(self, model):
        if model.menu_column_3:
            return FlatMenuItemSerializer(
                model.menu_column_3.menu_items.all(),
                many=True,
                read_only=True,
                context=self.context,
            ).data
        else:
            return []

    class Meta:
        model = FooterSettings
        fields = ("address_title", "address","phone_number", "website","social_links_title","facebook","instagram","twitter","pinterest","linked_in","youtube","email","menu_title_1","menu_column_1","menu_title_2","menu_column_2","menu_title_3","menu_column_3","copyright_line")


class GlobalSettingsSerializer(serializers.ModelSerializer):
    opengraph_image = ImageRenditionField(
        {"facebook": "fill-600x315-c0", "twitter": "fill-300x157-c0"}
    )

    class Meta:
        model = GlobalSettings
        fields = ("opengraph_image", "google_map_key", "google_analytic_tag")


class SettingsSerializer(serializers.Serializer):
    site = serializers.SerializerMethodField()
    footer = serializers.SerializerMethodField()
    main_menu = serializers.SerializerMethodField()

    def get_main_menu(self, model):
        site = Site.find_for_request(self.context["request"])
        try:
            main_menu = MainMenu.objects.get(site=site)
            settings = GlobalSettings.for_request(self.context["request"])
            main_menu_data = MainMenuItemSerializer(
                main_menu.menu_items.all(), context=self.context, many=True
            ).data
            return {
                "menu": main_menu_data,
                # "contact_page": settings.contact_page.get_url(self.context["request"]) if settings.contact_page else None,
                # "contact_page_label": settings.contact_page_label,
            }
        except Exception as e:
            raise e

    def get_footer(self, model):
        settings = FooterSettings.for_request(self.context["request"])
        return FooterSettingsSerializer(settings, context=self.context).data

    def get_site(self, model):
        site = Site.find_for_request(self.context["request"])
        settings = GlobalSettings.for_request(self.context["request"])

        return {
            "title": site.site_name,
            **GlobalSettingsSerializer(settings, context=self.context).data,
        }
