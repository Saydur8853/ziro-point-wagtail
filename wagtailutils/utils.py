from wagtail.models import Site
from wagtail.rich_text import expand_db_html

from wagtail.models import Site
from wagtail.rich_text import expand_db_html
import re
import logging

logger = logging.getLogger(__name__)

TOC_REGEX = re.compile('<h([1-6]) (.*?)data-block-key=\\"(.*?)\\"(.*?)>(.*?)</h[1-6]>')
SCRIPT_REGEX = re.compile('<script(.*?)src=\\"(.*?)\\"(.*?)>(.*?)</script>')


def prepare_richtext_for_api(value, request=None):
    if request:
        s = Site.find_for_request(request)
    else:
        s = Site.objects.get(is_default_site=True)
    current_site = s.root_url
    replace_text = 'src="{0}/'.format(current_site)
    replace_text2 = 'srcset="{0}/'.format(current_site)
    html_data = expand_db_html(value)
    html_data = html_data.replace('src="/', replace_text)
    html_data = html_data.replace('srcset="/', replace_text2)
    table_of_content = []
    scripts = []

    def heading_replacer(match):
        id = f"heading-{match.group(3)}"
        table_of_content.append(
            {"level": int(match.group(1)), "id": id, "text": match.group(5)}
        )
        return match.group().replace("data-block-key", f' id="{id}" data-block-key')

    def script_replacer(match):
        scripts.append(match.group(2))
        return ""

    if html_data:
        html_data = TOC_REGEX.sub(heading_replacer, html_data)
        html_data = SCRIPT_REGEX.sub(script_replacer, html_data)
    return {
        "content": html_data,
        "toc": table_of_content,
        "scripts": list(set(scripts)),
    }


def get_rendition_rules_for_article(style="default"):
    rendition_rules = None
    if style == "hero":
        rendition_rules = {
            "original": "fill-740x503-c0|format-webp",
            "original_fallback": "fill-740x503-c0",
            "tab": "fill-900x612-c0|format-webp",
            "tab_fallback": "fill-900x612-c0",
            "mobile": "fill-320x191-c0|format-webp",
            "mobile_fallback": "fill-320x191-c0",
        }
    elif style == "long":
        rendition_rules = {
            "original": "fill-193x240-c0|format-webp",
            "original_fallback": "fill-193x240-c0",
        }
    elif style == "default":
        rendition_rules = {
            "original": "fill-740x503-c0|format-webp",
            "original_fallback": "fill-740x503-c0",
            "tab": "fill-280x190-c0|format-webp",
            "tab_fallback": "fill-280x190-c0",
            "mobile": "fill-320x191-c0|format-webp",
            "mobile_fallback": "fill-320x191-c0",
        }
    elif style == "full_page":
        rendition_rules = {
            "original": "fill-1920x1080-c0|format-webp",
            "original_fallback": "fill-1920x1080-c0",
            "tab": "fill-1280x853-c0|format-webp",
            "tab_fallback": "fill-1280x853-c0",
            "mobile": "fill-640x427-c0|format-webp",
            "mobile_fallback": "fill-640x427-c0",
        }
    else:
        rendition_rules = {
            "original": "fill-480x286-c0|format-webp",
            "original_fallback": "fill-480x286-c0",
            "tab": "fill-450x268-c0|format-webp",
            "tab_fallback": "fill-450x268-c0",
            "mobile": "fill-123x153-c0|format-webp",
            "mobile_fallback": "fill-123x153-c0",
        }
    return rendition_rules


def get_page_api_cache_key(pk):
    return f"api:page_api:0:/api/v2/pages/{pk}/"

