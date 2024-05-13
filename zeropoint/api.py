from django.shortcuts import redirect
from wagtail.api.v2.views import PagesAPIViewSet as WagtailPagesAPIViewSet
from wagtail.api.v2.router import WagtailAPIRouter
from wagtail.api.v2.utils import BadRequestError, get_object_detail_url
from wagtail.images.api.v2.views import ImagesAPIViewSet
from wagtail.documents.api.v2.views import DocumentsAPIViewSet
from django.contrib.contenttypes.models import ContentType
from wagtail_headless_preview.models import PagePreview
from rest_framework.response import Response
from wagtail.api.v2.filters import (
    AncestorOfFilter,
    ChildOfFilter,
    DescendantOfFilter,
    LocaleFilter, 
    OrderingFilter,
    SearchFilter,
    TranslationOfFilter,
)
from .filters import FieldsFilter
from wagtail.models import Site
from wagtail.contrib.redirects.models import Redirect
from django.utils.decorators import method_decorator

# from custom_cache_page.cache import cache_page
from rest_framework.renderers import JSONRenderer
from django.http import Http404
import logging

logger = logging.getLogger(__name__)


class PagesAPIViewSet(WagtailPagesAPIViewSet):
    # renderer_classes = [JSONRenderer]

    filter_backends = [
        FieldsFilter,
        ChildOfFilter,
        AncestorOfFilter,
        DescendantOfFilter,
        OrderingFilter,
        TranslationOfFilter,
        LocaleFilter,
        SearchFilter,  # needs to be last, as SearchResults querysets cannot be filtered further
    ]
    filterset_fields = ["tags"]

    # @method_decorator(
    #     cache_page(
    #         timeout=60 * 60 * 24,
    #         key_func=lambda r: r.path,
    #         versioned=False,
    #         group_func=lambda r: "page_api",
    #         prefix="api",
    #     )
    # )
    # def detail_view(self, request, pk):
    #     return super().detail_view(request, pk)

    def check_query_parameters(self, queryset):
        """
        Ensure that only valid query parameters are included in the URL.
        """
        query_parameters = set(self.request.GET.keys())

        # All query parameters must be either a database field or an operation
        allowed_query_parameters = (
            set(self.get_available_fields(queryset.model, db_fields_only=True))
            .union(self.known_query_parameters)
            .union(set(getattr(queryset.model, "allowed_query_fields", {}).keys()))
        )
        unknown_parameters = query_parameters - allowed_query_parameters
        if unknown_parameters:
            raise BadRequestError(
                "query parameter is not an operation or a recognised field: %s"
                % ", ".join(sorted(unknown_parameters))
            )

    def find_object(self, queryset, request):
        site = Site.find_for_request(request)
        if "html_path" in request.GET and site is not None:
            path = request.GET["html_path"].rstrip("/")
            path_components = [component for component in path.split("/") if component]

            try:
                page, _, _ = site.root_page.specific.route(request, path_components)
            except Http404:
                try:
                    redirect = Redirect.objects.get(old_path=path)
                    return redirect.redirect_page
                except:
                    return

            if queryset.filter(id=page.id).exists():
                return page

        return super().find_object(queryset, request)

    def find_view(self, request):
        queryset = self.get_queryset()

        try:
            obj = self.find_object(queryset, request)

            if obj is None:
                raise self.model.DoesNotExist

        except self.model.DoesNotExist:
            raise Http404("not found")

        # Generate redirect
        url = get_object_detail_url(
            self.request.wagtailapi_router, request, self.model, obj.pk
        )

        if url is None:
            # Shouldn't happen unless this endpoint isn't actually installed in the router
            raise Exception(
                "Cannot generate URL to detail view. Is '{}' installed in the API router?".format(
                    self.__class__.__name__
                )
            )

        if request.query_params.get("redirect", "true") == "false":
            request.parser_context["kwargs"]["pk"] = obj.pk
            self.request = request
            serializer = self.get_serializer(obj)
            # logger.critical(serializer.data)
            return Response(serializer.data)
        else:
            return redirect(url)


class PagePreviewAPIViewSet(WagtailPagesAPIViewSet):
    known_query_parameters = WagtailPagesAPIViewSet.known_query_parameters.union(
        ["content_type", "token"]
    )

    def listing_view(self, request):
        page = self.get_object()
        serializer = self.get_serializer(page)
        return Response(serializer.data)

    def detail_view(self, request, pk):
        page = self.get_object()
        serializer = self.get_serializer(page)
        return Response(serializer.data)

    def get_object(self):
        app_label, model = self.request.GET["content_type"].split(".")
        content_type = ContentType.objects.get(app_label=app_label, model=model)

        page_preview = PagePreview.objects.get(
            content_type=content_type, token=self.request.GET["token"]
        )
        page = page_preview.as_page()
        if not page.pk:
            # fake primary key to stop API URL routing from complaining
            page.pk = 0

        return page


# Create the router. "wagtailapi" is the URL namespace
api_router = WagtailAPIRouter("wagtailapi")

# Add the three endpoints using the "register_endpoint" method.
# The first parameter is the name of the endpoint (eg. pages, images). This
# is used in the URL of the endpoint
# The second parameter is the endpoint class that handles the requests
api_router.register_endpoint("pages", PagesAPIViewSet)
api_router.register_endpoint("images", ImagesAPIViewSet)
api_router.register_endpoint("documents", DocumentsAPIViewSet)
api_router.register_endpoint("page_preview", PagePreviewAPIViewSet)
