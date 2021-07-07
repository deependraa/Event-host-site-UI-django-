from django.http.response import HttpResponseRedirect
from home.models import event
from django.shortcuts import get_object_or_404, render
from . import urls
from django.urls import reverse
from django.contrib import messages , auth

# Create your views here.


def home(request):
    all_obj =event.objects.order_by('-Date')
    content = {
        'all_obj' : all_obj,
    }
    return render(request ,'home/home.html',content)

def events(request,event_id):
    Sevent = get_object_or_404(event, pk = event_id)
    Sevent.likes.add(request.user)
    return render(request,'home/single_event.html')

def likeview(request,pk):
    post = get_object_or_404(event, id=request.POST.get('event_id'))
    post.likes.add(request.user)
    return HttpResponseRedirect(reverse('likeview',args=[str(pk)]))