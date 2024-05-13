from rest_framework.filters import BaseFilterBackend
from taggit.managers import TaggableManager
import logging
from django.db import models
from wagtail.api.v2.utils import BadRequestError, parse_boolean

logger = logging.getLogger(__name__)


class FieldsFilter(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        """
        This performs field level filtering on the result set
        Eg: ?title=James Joyce
        """
        fields = set(view.get_available_fields(
            queryset.model, db_fields_only=True))
        allowed_fields = getattr(queryset.model, "allowed_query_fields", {})
        # logger.critical(allowed_fields)
        allowed_fields_keys = set(allowed_fields.keys())

        # Locale is a database field, but we provide a separate filter for it
        if "locale" in fields:
            fields.remove("locale")

        for field_name, value in request.GET.items():
            if field_name in allowed_fields_keys:
                field_description = allowed_fields[field_name]
                lookup_type = field_description.get("type", "string")
                if lookup_type == "list_of_string":
                    value = [x.strip() for x in value.split(",")]
                elif lookup_type in ["list_of_id", "list_of_int"]:
                    value = [int(x.strip()) for x in value.split(",")]
                elif lookup_type == "list_of_float":
                    value = [float(x.strip()) for x in value.split(",")]
                elif lookup_type == "float":
                    value = float(value)
                elif lookup_type == "int" or lookup_type == "id":
                    value = int(value)

                if type(field_description["lookup"]) == str:
                    queryset = queryset.filter(
                        **{field_description["lookup"]: value})
                else:
                    queryset = field_description["lookup"](queryset, value)
            elif field_name in fields:
                try:
                    field = queryset.model._meta.get_field(field_name)
                except LookupError:
                    field = None

                # Convert value into python
                try:
                    if isinstance(
                        field, (models.BooleanField, models.NullBooleanField)
                    ):
                        value = parse_boolean(value)
                    elif isinstance(field, (models.IntegerField, models.AutoField)):
                        value = int(value)
                    elif isinstance(field, models.ForeignKey):
                        value = field.target_field.get_prep_value(value)
                except ValueError as e:
                    raise BadRequestError(
                        "field filter error. '%s' is not a valid value for %s (%s)"
                        % (value, field_name, str(e))
                    )

                if isinstance(field, TaggableManager):
                    for tag in value.split(","):
                        queryset = queryset.filter(
                            **{field_name + "__name": tag})

                    # Stick a message on the queryset to indicate that tag filtering has been performed
                    # This will let the do_search method know that it must raise an error as searching
                    # and tag filtering at the same time is not supported
                    queryset._filtered_by_tag = True
                else:
                    queryset = queryset.filter(**{field_name: value})

        return queryset