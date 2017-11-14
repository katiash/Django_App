# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import HttpResponse, redirect ### NEW LINE ADDED!

# Create your views here.

def index(request):
    response = "Placeholder to later display all the list of blogs"
    return HttpResponse(response)

def new(request):
    response = "placeholder to display a new form to create a new blog"
    return HttpResponse(response)

def create(request):
    print "I am in create method"
    return redirect('/')

def show(request, number):
    print number
    response = "placeholder to display blog " + number
    return HttpResponse(response)

def edit(request, number):
    return HttpResponse("placeholder to edit blog " + number)

def destroy(request, number):
    return redirect('/')


