from django.shortcuts import render

# Create your views here.


def dashboardview(request):
    return render(request, 'Dashboard/dashboard.html')
