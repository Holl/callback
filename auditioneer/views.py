import json
from django.http import HttpResponse
from django.shortcuts import render, redirect
from accounts_manager.models import ProductionProfile, ActorProfile
from auditioneer.forms import AuditionForm, PartForm
from auditioneer.models import Audition



def angular(request):
    try:
        dataums = {'info': request.user.actor.id}
    except:
        dataums = {'info': request.user.producer.id}
    return render(request, 'angular.html', dataums)



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


def check_login(request):
    if request.user.is_authenticated():
        return HttpResponse(json.dumps({'result': {'logged': True}, 'user': request.user.username}),
                        content_type="application/json")
    else:
        return HttpResponse(json.dumps({'result': {'logged': False}}),
                        content_type="application/json")
