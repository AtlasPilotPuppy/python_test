# Create your views here.

from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseBadRequest
from django.views.decorators.http import require_http_methods
from django.views.generic import ListView
from todo.models import *
from todo.forms import *

def register(request):
    if request.method == 'POST':
        user_form  = UserForm(request.Post, prefix='user')
        profile_form = UserProfileForm(request.Post, prefix='profile')
        if user_form.is_valid() and profile_form.is_valide():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            return HttpResponseRedirect(reverse('tasklist'))
    else:
        user_form = UserForm(prefix='user')
        profile_form = UserProfileForm(prefix='profile')
    return render_to_response('register.html', dict(userform = user_form,
                                                   profileform = profile_form),
                              context_instance = RequestContext(request))

@login_required
def tasklist(request):
    u = request.user
    # show tasks in reverse chronological order with compeleted tasks at the
    # bottom.
    tasks = Task.objects.filter(user = u).order_by('completed', '-pk')
    return render_to_response("todo.html",
                              {'tasks':tasks}, 
                              RequestContext(request))
@require_http_methods(['POST'])
def delete_task(request):
    task_pk = request.POST.get('task_pk')
    try:
        t = Task.objects.get(pk=task_pk)
        t.delete()
    except Task.DoesNotExist:
        # we can't find the task.
        return HttpResponseBadRequest()

    # delete succeeded, nothing to return.
    return HttpResponse()

@require_http_methods(['POST'])
def toggle_task(request):
    task_pk = request.POST.get('task_pk')
    try:
        t = Task.objects.get(pk=task_pk)
        t.completed = not t.completed
        t.save()
    except Task.DoesNotExist:
        # we can't find the task
        return HttpResponseBadRequest()

    # update successful, nothing to return.
    return HttpResponse()

@require_http_methods(['POST'])
def create_task(request):
    u = request.user
    t = request.POST.get('task')
    print t
    try:
        t = Task.objects.create(user=u, text=t)
        t.save()
        key = t.pk
        return HttpResponse(key)
    except:
        # we can't create the task
        return HttpResponseBadRequest()

    # update successful, nothing to return.
    return HttpResponse()
