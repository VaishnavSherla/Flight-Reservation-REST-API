from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import FlightViewSet, PassengerViewSet, ReservationViewSet
from .views import find_flights, save_reservation
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register('flights', FlightViewSet)
router.register('passengers', PassengerViewSet)
router.register('reservations', ReservationViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('token/', obtain_auth_token, name='api-token'),
    path('findFlights/', find_flights),
    path('saveReservation/', save_reservation)
]
