from django.shortcuts import render, redirect
from auditioneer.forms import AuditionForm, PartForm


def angular(request):
    return render(request, 'angular.html')


def audition_builder(request):
    if request.method == "POST":
        form = AuditionForm(request.POST)
        if form.is_valid():
            submission = form.save(commit=False)
            usr = request.user
            submission.user = usr
            submission.save()
            return redirect('/')
    else:
        form = AuditionForm
    dataums = {'form': form}
    return render(request, 'audition_builder.html', dataums)

def part_builder(request):
    if request.method == "POST":
        form = PartForm(request.POST)
        if form.is_valid():
            return redirect('/')
    else:
        form = PartForm
    dataums = {'form': form}
    return render(request, 'audition_builder.html', dataums)
