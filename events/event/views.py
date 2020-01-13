from django.shortcuts import render,redirect
from event.models import *
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# Create your views here.
from django.template.loader import get_template
from django.http import JsonResponse
from django.contrib.auth import login, authenticate
from event.forms import EventForm,RegistrationForm
from .serializers import EventSerializer
from django.http import JsonResponse
from django.http import HttpResponse
from rest_framework.response import Response
def home(request):
    return render(request,'home.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('signin')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})
def signin(request):
    if request.method == "POST":
        try:
            username=request.POST['username']
            raw_password=request.POST['password']
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            request.session['username'] = username
            return redirect('postpages')
        except:
            return render(request,'registration/login.html')
    return render(request,'registration/login.html/')

def validate_username(request):
    username = request.GET.get('username', None)
    data = {
        'is_taken': User.objects.filter(username__iexact=username).exists()
    }
    if data['is_taken']:
        data['error_message'] = 'A user with this username already exists.'
        return JsonResponse(data)

def create_event(request):
    form=EventForm()
    user=User.objects.get(username=request.user)
    if request.method=='POST':
        form=EventForm(request.POST)
        if form.is_valid():
            obj=form.save(commit=False)
            obj.user_id=user
            obj.save()
            return redirect('view1')
    else:
        return render(request,'create_event.html',{'form':form})
import json
def view1(request):
    return render(request,'event.html')
from rest_framework.decorators import api_view, renderer_classes

@api_view(('GET',))

def view_event(request):

        user=request.user
        public=Event.objects.all()
        serializer=EventSerializer(public,many=True)

        return Response(serializer.data)
def register(request):
    if request.method == "POST":
        user=request.user
        event_name = request.POST.get('event_name')
        event=Event.objects.get(event_name=event_name)

        no_of_attendees =event.no_of_attendees

        registers= Registration.objects.filter(event_id=event.event_id,user_id=user)

        no_of_presence=len(registers)
        #user_find=Registration.objects.filter(event_=event.event_date,user_id=user,none=True)

        if no_of_attendees>no_of_presence:
            registration=Registration.objects.create(event_id=event,user_id=user)
            return redirect('view1')
        else:
            return HttpResponse('seats already full')
        

def delete(request):
    if request.method=='POST':
        event_name = request.POST.get('event_name')
        event = Event.objects.get(event_name=event_name)
        event.delete()
        return HttpResponse('deleted!')


