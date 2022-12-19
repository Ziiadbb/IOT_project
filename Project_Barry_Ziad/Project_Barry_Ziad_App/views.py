from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import render
from .models import Dht


def home(request):
    return HttpResponse('bonjour à tous')

def test(request):
    tab = Dht.objects.all()
    s = {'tab': tab}
    return render(request, 'app.html', s)

# Create your views here.
