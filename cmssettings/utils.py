def get_google_maps_api_key():
    from wagtail.models import Site
    from cmssettings.models import GlobalSettings
    site = Site.objects.filter(is_default_site=True).first()
    settings = GlobalSettings.for_site(site=site)
    return settings.google_map_key