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
from .forms import (
    EssayCreateForm
)
from .models import (
    Essay
)
from station.models import (
    Station
)
from .serializers import (
    EssaySerializer, EssayCreateSerializer
)


# Global variables


# Views
''' Home page '''
def home(request, *args, **kwargs):
    search_essay = Essay.objects.all()
    search_station = Station.objects.all()
    DATA = {
        'message':'All clear!',
        'status':200,
        'essay':search_essay,
        'station':search_station
    }
    return render(request, 'home.html', context=DATA)

''' Create essay form '''
@permission_classes([IsAuthenticated])
def form_essay_create(request, *args, **kwargs):
    if not request.user.is_authenticated:
        DATA = {
            'message':'Not authenticated!',
            'status': 401
        }
        return render(request, 'home.html', context=DATA)
    else:
        _U = request.user
        FORM = EssayCreateForm(request.POST or None)
        goto = request.POST.get('next') or None
        DATA = {
            'formName':'Create New Essay',
            'form':FORM
        }
        if FORM.is_valid():
            form_data = FORM.save(commit=False)
            form_data.user = _U
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
        return render(request, 'jsys/internal_essay_create.html', context=DATA)


''' View individual essay '''
def form_essay_view(request, essayID, *args, **kwargs):
    search_essay = Essay.objects.filter(id=essayID).first()
    if not search_essay:
        DATA = {
            'error': f'essayID [{essayID}] does not exist',
            'status': 404
        }
        return JsonResponse(DATA)

    else:
        DATA = {
            'id': search_essay.id,
            'user': search_essay.user.username,
            'title': search_essay.title,
            'content': search_essay.content,
            'status': 200
        }
        return render(request, 'jsys/internal_essay_view.html', context={'essay':search_essay})
