# Imports
'''3rd Party'''
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
'''Django official'''
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render, redirect
'''Project related'''
from .forms import (StationCreateForm)
from station.models import (Station)


# Global variables


# Views
''' Create station form '''
@permission_classes([IsAuthenticated])
def form_station_create(request, *args, **kwargs):
    if not request.user.is_authenticated:
        DATA = {
            'message':'Not authenticated!',
            'status': 401
        }
        return render(request, 'home.html', context=DATA)
    else:
        _U = request.user
        FORM = StationCreateForm(request.POST or None)
        goto = request.POST.get('next') or None
        DATA = {
            'formName':'Register New Station',
            'form':FORM
        }
        if FORM.is_valid():
            form_data = FORM.save(commit=False)
            form_data.founder = _U
            form_data.save()
            return redirect(goto)
        elif FORM.errors:
            DATA['errors'] = FORM.errors
        elif not FORM:
            DATA = {
                'message':'Something went majorly wrong',
                'status':500
            }
            return render(request, 'home.html', context=DATA)
        return render(request, 'jsys/internal_station_create.html', context=DATA)
