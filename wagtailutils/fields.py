from collections import OrderedDict

from rest_framework.fields import Field
from wagtail.images.models import SourceImageIOError
from wagtail.images.views.serve import generate_image_url


class ImageRenditionField(Field):
    def __init__(self, filter_specs, *args, cache_renditions=False, **kwargs):
        self.filter_specs = filter_specs or {"original": "original"}
        super().__init__(*args, **kwargs)

    def to_representation(self, value):
        try:
            data = {
                "id": value.id,
                "alt": value.title,
                "width": value.width,
                "height": value.height,
                "renditions": {},
            }
            for name, rule in self.filter_specs.items():
                data["renditions"][name] = generate_image_url(value, rule)
            return data
        except SourceImageIOError:
            return OrderedDict(
                [
                    ("error", "SourceImageIOError"),
                ]
            )
