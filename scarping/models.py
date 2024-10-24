from django.db import models

class Car(models.Model):
    brand = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    car_class = models.CharField(max_length=255)
    fuel = models.CharField(max_length=255)
    seat_count = models.IntegerField()
    segment = models.CharField(max_length=255)
    transmission = models.CharField(max_length=255)
    vendor = models.CharField(max_length=255)
    check_in_datetime = models.DateTimeField()
    check_in_office = models.CharField(max_length=255)
    check_out_datetime = models.DateTimeField()
    check_out_office = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.check_in_office} {self.model}"
