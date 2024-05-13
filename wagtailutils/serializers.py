from rest_framework import serializers
from wagtailmenus.conf import settings
from wagtail.models import Page
from wagtailmenus.models import MainMenuItem, FlatMenuItem
from wagtail.contrib.redirects.models import Redirect

import logging

from wagtailutils.fields import ImageRenditionField

logger = logging.getLogger()

MENU_IMAGE_RENDITION_SPEC = getattr(
    settings,
    "WAGTAILUTILS_MENU_IMAGE_RENDITIONS",
    {"original": "width-800|format-webp", "original_fallback": "width-800"},
)


class MenuPageChildSerializer(serializers.ModelSerializer):
    label = serializers.ReadOnlyField(source="title")
    link = serializers.SerializerMethodField()
    children = serializers.SerializerMethodField()
    additional_data = serializers.SerializerMethodField()
    image = serializers.SerializerMethodField()
    is_collection = serializers.SerializerMethodField()

    def get_is_collection(self, model):
        return getattr(model.specific, "is_collection", False)

    def get_link(self, model):
        return model.specific.get_url()

    def get_children(self, model):
        try:
            return model.specific.get_menu_children(context=self.context)
        except:
            children = Page.objects.child_of(model).filter(show_in_menus=True)
            return MenuPageChildSerializer(children, many=True).data

    def get_additional_data(self, model):
        try:
            return model.specific.additional_menu_data(context=self.context)
        except:
            return None

    def get_image(self, model):
        image = getattr(model.specific, "menu_image", False)
        if image:
            return ImageRenditionField(MENU_IMAGE_RENDITION_SPEC).to_representation(
                image
            )
        return None

    class Meta:
        model = Page
        fields = (
            "id",
            "label",
            "link",
            "children",
            "additional_data",
            "image",
            "is_collection",
        )


class MainMenuItemSerializer(serializers.ModelSerializer):
    link = serializers.SerializerMethodField()
    label = serializers.SerializerMethodField()
    num_of_child = serializers.SerializerMethodField()
    children = serializers.SerializerMethodField()
    is_external = serializers.SerializerMethodField()
    additional_data = serializers.SerializerMethodField()
    is_collection = serializers.SerializerMethodField()

    def get_is_collection(self, model):
        if model.link_page:
            return getattr(model.link_page.specific, "is_collection", False)
        return False

    def get_additional_data(self, model):
        if model.link_page:
            try:
                return model.link_page.specific.additional_menu_data(
                    context=self.context
                )
            except:
                return None
        return None

    def get_is_external(self, model):
        return True if model.link_url else False

    def get_label(self, model):
        return model.link_text or model.link_page.title

    def get_link(self, model):

        return model.link_url or model.link_page.specific.get_url(
            self.context["request"]
        )

    def get_num_of_child(self, model):
        try:
            count = (
                Page.objects.child_of(model.link_page)
                .filter(show_in_menus=True)
                .count()
            )
        except Exception:
            count = 0
        return count

    def get_children(self, model):
        if model.allow_subnav and model.link_page:
            try:
                return model.link_page.specific.get_menu_children(context=self.context)
            except:
                children = Page.objects.child_of(model.link_page).filter(
                    show_in_menus=True
                )
                return MenuPageChildSerializer(children, many=True).data
        else:
            return []

    class Meta:
        model = MainMenuItem
        fields = (
            "id",
            "link",
            "url_append",
            "handle",
            "label",
            "num_of_child",
            "children",
            "is_external",
            "additional_data",
            "is_collection",
        )


class FlatMenuItemSerializer(serializers.ModelSerializer):
    link = serializers.SerializerMethodField()
    label = serializers.SerializerMethodField()
    is_external = serializers.SerializerMethodField()

    def get_is_external(self, model):
        return True if model.link_url else False

    def get_label(self, model):
        return model.link_text or model.link_page.title

    def get_link(self, model):
        return model.link_url or model.link_page.get_url(self.context["request"])

    class Meta:
        model = FlatMenuItem
        fields = ("id", "link", "url_append", "handle", "label", "is_external")


class FlatMenuSerializer(serializers.ModelSerializer):
    menu_items = serializers.SerializerMethodField()

    def get_menu_items(self, instance):
        flat_menu_items = getattr(instance, settings.FLAT_MENU_ITEMS_RELATED_NAME).all()
        return FlatMenuItemSerializer(
            flat_menu_items, context=self.context, many=True
        ).data

    class Meta:
        model = None
        fields = "__all__"


class RedirectPageSerializer(serializers.ModelSerializer):
    link = serializers.SerializerMethodField()

    def get_link(self, model):
        if model.redirect_page:
            return {"type": "internal", "link": model.redirect_page.url}
        elif model.redirect_link:
            return {"type": "external", "link": model.redirect_link}
        return None

    class Meta:
        model = Redirect
        fields = ("is_permanent", "link")
