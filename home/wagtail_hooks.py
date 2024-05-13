from .models import Newsletter
from wagtail.contrib.modeladmin.options import (
    ModelAdmin, modeladmin_register,
)



class NewsletterSubscriberAdmin(ModelAdmin):
    model = Newsletter
    menu_label = "Subscribers"
    menu_icon = "group"
    add_to_settings_menu = False
    list_display = ("email", "subscribed_at")
    search_fields = ("email", "subscribed_at")

modeladmin_register(NewsletterSubscriberAdmin)