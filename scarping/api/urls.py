from django.urls import path
from scarping.api.views import (
    AutoComplete360,
    CarFilterViewSet,
    AutocompleteEnUygun,
    AutoCompleteObilet,
)

urlpatterns = [
    path(
        "filter/",
        CarFilterViewSet.as_view({"post": "search"}),
        name="car-rental-filter",
    ),
    path(
        "auto360/",
        AutoComplete360.as_view({"get": "autocomplete"}),
        name="autocomplete",
    ),
    path(
        "autoenuygun/",
        AutocompleteEnUygun.as_view({"get": "autocomplete"}),
        name="autocomplete",
    ),
    path(
        "autobilet/",
        AutoCompleteObilet.as_view({"get": "autocomplete"}),
        name="autocomplete",
    ),
    path(
        "filter/results/",
        CarFilterViewSet.as_view({"get": "get_filtered_results"}),
        name="car-rental-filter-results",
    ),
]
