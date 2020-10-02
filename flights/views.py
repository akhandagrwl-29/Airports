from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse


from flights.models import Flight,Passengers
# Create your views here.
def index(request):
    return render(request,"flights/index.html",{
        "flights":Flight.objects.all()
    })
    
def flight(request, flightid):
    flight=Flight.objects.get(id=flightid)
    return render(request,"flights/flight.html",{
        "flight":flight,
        "passengers":flight.passengers.all(),
        "non_passengers":Passengers.objects.exclude(flight=flight).all()
    })
    
def book(request,flightid):
    if request.method=="POST":
        flight=Flight.objects.get(pk=flightid)
        passenger=Passenger.object.get(pk=int(request.POST["passenger"]))
        Passengers.flights.add(flight);
        return HttpResponseRedirect(reverse("flight",args(flight.id)))
    
    