from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import FlightViewSet, PassengerViewSet, ReservationViewSet
from .views import find_flights, save_reservation
from rest_framework.authtoken.views import obtain_auth_token

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

router = DefaultRouter()
router.register('flights', FlightViewSet)
router.register('passengers', PassengerViewSet)
router.register('reservations', ReservationViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('findFlights/', find_flights),
    path('saveReservation/', save_reservation),

    path('users/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('users/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('users/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
