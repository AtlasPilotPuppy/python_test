import json

from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.views.decorators.csrf import csrf_exempt


from applications.userprofile.models import Userprofile, Todo
from applications.userprofile.forms import Userform

def home(request):
    return render_to_response('home.html',
                          {},
                          context_instance=RequestContext(request))
    
def login(request):
    if request.method == "GET":
        return render_to_response('login.html',
                          {},
                          context_instance=RequestContext(request))
    
    elif request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
    
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                auth_login(request, user)
                return HttpResponseRedirect("/")
                
        return render_to_response('login.html',
                          {'errors':True},
                          context_instance=RequestContext(request))

def register(request):
    if request.method == "GET":
        form = Userform()
        return render_to_response('register.html',
                          {'form':form},
                          context_instance=RequestContext(request))
    
    elif request.method == "POST":
        form = Userform(request.POST)
        if not form.is_valid():
            return render_to_response('register.html',
                      {'form':form},
                      context_instance=RequestContext(request))
        else:
            up = form.save()
            
            auth_login(request, up.user)
            return HttpResponseRedirect("/")
        

def logout(request):
    auth_logout(request)
    return HttpResponseRedirect("/login")

def todo(request):
    list, created = Todo.objects.get_or_create(user = request.user)
    list = list.get_list() 
    return render_to_response('todo.html',
                          {'list':list},
                          context_instance=RequestContext(request))

@csrf_exempt
def save_todo(request):
    item = request.POST.get('todo')
    if item:
        todo = Todo.objects.get(user=request.user)
        todo.add(item)
    return HttpResponse(json.dumps({"success":True}), mimetype="application/json")

@csrf_exempt
def update_todo(request):
    item = request.POST.get('todo')
    if item:
        todo = Todo.objects.get(user=request.user)
        status = todo.update(item)
    return HttpResponse(json.dumps({"success":True, 'status':status}), mimetype="application/json")

@csrf_exempt
def remove_todo(request):
    item = request.POST.get('todo')
    if item:
        todo = Todo.objects.get(user=request.user)
        status = todo.remove(item)
    return HttpResponse(json.dumps({"success":True}), mimetype="application/json")

