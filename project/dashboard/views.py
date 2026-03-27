from django.shortcuts import render
from .models import Car

# Create your views here.
def Overview(request):

    my_cars = Car.objects.filter(user = request.user)
    return render(request, 'overview.html', {'data':my_cars})

def SlotBooking(request):
    pass

def ServiceHistory(request):
    pass

def Notifications(request):
    pass

def Settings(request):
    pass
