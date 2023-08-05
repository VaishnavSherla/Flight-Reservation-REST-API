from django.db import models

# Create your models here.
class Flight(models.Model):
    flightNumber = models.CharField(max_length=10)
    operatingAirlines = models.CharField(max_length=20)
    departureCity = models.CharField(max_length=20, blank=True, null=True)
    arrivalCity = models.CharField(max_length=20)
    dateOfDeparture = models.DateField()
    estimatedTimeOfDeparture = models.TimeField()

    def __str__(self):
        return f"{self.flightNumber} - {self.departureCity} to {self.arrivalCity}"

class Passenger(models.Model):
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    middleName = models.CharField(max_length=20, null=True)
    email = models.EmailField(max_length=30)
    phone = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.firstName} {self.middleName} {self.lastName}"


class Reservation(models.Model):
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    passenger = models.ForeignKey(Passenger, on_delete=models.CASCADE)
