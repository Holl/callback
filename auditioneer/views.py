from django.shortcuts import render, redirect
from accounts_manager.models import ProductionProfile
from auditioneer.forms import AuditionForm, PartForm
from auditioneer.models import Audition



def angular(request):
    return render(request, 'angular.html')


def audition_builder(request):
    if request.method == "POST":
        form = AuditionForm(request.POST)
        if form.is_valid():
            submission = form.save(commit=False)
            usr = request.user
            submission.production_user = ProductionProfile.objects.get(user=usr)
            submission.save()
            return redirect('/')
    else:
        form = AuditionForm
    dataums = {'form': form}
    return render(request, 'audition_builder.html', dataums)

def part_builder(request, audition_id):
    if request.method == "POST":
        form = PartForm(request.POST)
        if form.is_valid():
            submission = form.save(commit=False)
            AUD = Audition.objects.get(id=audition_id)
            submission.audition = AUD
            submission.save()
            return redirect('/')
        else:
            return redirect('/login')
    else:
        form = PartForm
    dataums = {'form': form}
    return render(request, 'part_builder.html', dataums)
