from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from accountapp.models import HelloWorld


def hello_world(request):
    if request.method == "POST":

        temp = request.POST.get('input')

        new_data = HelloWorld()
        new_data.text = temp
        new_data.save()

        return render(request, 'accountapp/hello_world.html',
                      context={'new_data': new_data})
    else:
        return render(request, 'accountapp/hello_world.html',
                      context={'text': 'GET METHOD!'})
