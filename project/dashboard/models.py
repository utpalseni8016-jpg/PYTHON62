from django.db import models
from django.contrib.auth.models import User

class Car(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="cars")

    name = models.CharField(max_length=100)  # Tesla Model Y
    image = models.ImageField(upload_to='cars/')

    max_speed = models.IntegerField()  # 340 km/h
    engine = models.CharField(max_length=100)  # En12 87
    charging_port = models.CharField(max_length=100)  # A3 EV 883
    maintenance_cycle = models.CharField(max_length=50)  # Every 1 month
    seat_capacity = models.IntegerField()  # 10+
    audio_system = models.CharField(max_length=100)  # Sony 325i

    battery_percentage = models.IntegerField(default=0)  # 56%
    is_charging = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} - {self.user.username}'