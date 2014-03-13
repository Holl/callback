from django.shortcuts import render


def angular(request):
    return render(request, 'angular.html')
