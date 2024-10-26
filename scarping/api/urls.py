from django.urls import path
from scarping.api.views import CarRentalViewSet, AutoComplete, CarRentalEnViewSet,CarFilterViewSet,AutocompleteViewSet,CarRentalAPIView

urlpatterns = [
#     path('api/', CarRentalViewSet.as_view({'post': 'search'}), name='car-rental-search'),
#     path('api/filter/', CarRentalViewSet.as_view({'get': 'filter'}), name='car-rental-filter'),
    path('api/',CarRentalViewSet.as_view({'post':'search'}),name='car-rental-search'), 
    path('filter/',CarFilterViewSet.as_view({'post':'search'}),name='car-rental-filter'),
    path('autocomplete/', AutoComplete.as_view({'get': 'autocomplete'}), name='autocomplete'),
    path('auto/', AutocompleteViewSet.as_view({'get': 'autocomplete'}), name='autocomplete'),
    path('api/car/', CarRentalAPIView.as_view(), name='car-data'),
    path('filter/results/', CarFilterViewSet.as_view({'get': 'get_filtered_results'}), name='car-rental-filter-results'),
]
