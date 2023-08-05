from django.shortcuts import render
from .serializers import FlightSerializer, PassengerSerializer, ReservationSerializer
from .models import Flight, Passenger, Reservation
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

# Create your views here.
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def find_flights(request):
    departure_city = request.data.get('departureCity')
    arrival_city = request.data.get('arrivalCity')
    date_of_departure = request.data.get('dateOfDeparture')

    # Start with all flights
    flights = Flight.objects.all()

    # Filter flights based on the provided data
    if departure_city:
        flights = flights.filter(departureCity=departure_city)
    if arrival_city:
        flights = flights.filter(arrivalCity=arrival_city)
    if date_of_departure:
        flights = flights.filter(dateOfDeparture=date_of_departure)

    serializer = FlightSerializer(flights, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def save_reservation(request):
    try:
        flight = Flight.objects.get(id=request.data['flightId'])
    except Flight.DoesNotExist:
        return Response({"error": "Flight not found"}, status=status.HTTP_404_NOT_FOUND)
    
    first_name = request.data.get('firstName')
    last_name = request.data.get('lastName')
    phone = request.data.get('phone')

    # Check if first name and last name are the same
    if first_name and last_name and first_name.lower() == last_name.lower():
        return Response({"error": "First name and last name cannot be the same."}, status=status.HTTP_400_BAD_REQUEST)

    # Check if phone number is valid (10 digits)
    if len(phone) != 10 or not phone.isdigit():
        return Response({"error": "Invalid phone number. Phone number must be 10 digits long and contain only numeric digits."}, status=status.HTTP_400_BAD_REQUEST)
    
    passenger = Passenger()
    passenger.firstName = request.data['firstName']
    passenger.lastName = request.data['lastName']
    passenger.middleName = request.data['middleName']
    passenger.phone = request.data['phone']
    passenger.email = request.data['email']
    passenger.save()

    reservation = Reservation()
    reservation.flight = flight
    reservation.passenger = passenger

    Reservation.save(reservation)

    return Response(status=status.HTTP_201_CREATED)
    
class FlightViewSet(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
    permission_classes = [IsAuthenticated]

class PassengerViewSet(viewsets.ModelViewSet):
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer
    permission_classes = [IsAuthenticated]


class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    permission_classes = [IsAuthenticated]
