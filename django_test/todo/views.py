from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm 
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
        form  = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            u = authenticate(username=form.data['email'], password=form.data['password'])
            print form.data['email']
            print form.data['password']
            print u
            auth.login(request, u)        
            return HttpResponseRedirect('/todo/')
        else:
            return render_to_response('register.html', {'form' : form},
                              context_instance = RequestContext(request))
    else:
        print "Construct empty form"
        form = UserForm()
    return render_to_response('register.html', {'form':form}, RequestContext(request) )
    
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/todo/')
                              
def login(request):
    """Handles the logic for logging a user into the system."""
    if request.method != 'POST':
        form = AuthenticationForm()
        return render_to_response('login.html',
                {'form': form}, RequestContext(request))
            
    username = request.POST.get('username')
    password = request.POST.get('password')
    u = authenticate(username=username, password=password)
    if u is not None:
        if u.is_active:
            auth.login(request, u)
        else:
            form = AuthenticationForm(data=request.POST)
            return render_to_response('login.html',
            {'form': form}, RequestContext(request))    
            
#    next = request.POST.get('next')
    return HttpResponseRedirect('/todo/')

@login_required(login_url='/todo/login/')
def tasklist(request):
    u = request.user
    # show tasks in reverse chronological order with compeleted tasks at the
    # bottom.
    tasks = Task.objects.filter(user = u).order_by('completed', '-pk')
    return render_to_response("todo.html",
                              {'tasks':tasks}, 
                              RequestContext(request))

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
    
@require_http_methods(['POST'])
def toggle_task(request):
    task_pk = request.POST.get('task_pk')
    print task_pk, type(task_pk)
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

