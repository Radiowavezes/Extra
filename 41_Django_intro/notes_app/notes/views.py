from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Notes
from datetime import datetime


def index(request):
    my_notes = Notes.objects.all()
    template = loader.get_template('index.html')
    context = {
        'my_notes': my_notes
    }
    return HttpResponse(template.render(context, request))

def create(request):
    template = loader.get_template('create.html')
    return HttpResponse(template.render({}, request))

def create_data(request):
    new_text = request.POST['text']
    new_title = request.POST['title']
    dt = request.POST.get('pub_date')
    rmndr = request.POST.get('reminder')
    new_note = Notes(text = new_text, title=new_title, pub_date = dt, reminder=rmndr)
    new_note.save()
    return HttpResponseRedirect(reverse('index'))

def update(request, id_num):
    update_note = Notes.objects.get(id=id_num)
    template = loader.get_template('update.html')
    context = {
        'note': update_note
    }
    return HttpResponse(template.render(context, request))

def update_data(request, id_num):
    new_text = request.POST['text']
    new_title = request.POST['title']
    update_note = Notes.objects.get(id=id_num)
    update_note.text = new_text
    update_note.title = new_title
    update_note.save()
    return HttpResponseRedirect(reverse('index'))

def delete(request, id_num):
    delete_note = Notes.objects.get(id=id_num)
    delete_note.delete()
    return HttpResponseRedirect(reverse('index'))
