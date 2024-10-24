from django.urls import path
from scarping.api.views import CarRentalViewSet, AutoComplete, CarRentalEnViewSet

urlpatterns = [
#     path('api/', CarRentalViewSet.as_view({'post': 'search'}), name='car-rental-search'),
#     path('api/filter/', CarRentalViewSet.as_view({'get': 'filter'}), name='car-rental-filter'),
    path('api/',CarRentalViewSet.as_view({'post':'search'}),name='car-rental-search'), 
    path('api/filter/', CarRentalViewSet.as_view({'get': 'filter'}), name='car-rental-filter'),
    path('autocomplete/', AutoComplete.as_view({'get': 'autocomplete'}), name='autocomplete'),
    path('enuygun/', CarRentalEnViewSet.as_view({'post': 'search'}), name='car-rental-enuygun'),
]
