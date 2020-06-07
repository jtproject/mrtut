# Imports
'''3rd Party'''
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
'''Django official'''
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render
'''Project related'''
from .forms import (
    EssayCreateForm
)
from .models import (
    Essay
)
from .serializers import (
    EssaySerializer, EssayCreateSerializer
)


# Global variables


# Views
''' Home page '''
def home(request, *args, **kwargs):
    search_essay = Essay.objects.all()
    return render(request, 'home.html', context={'message':'Everything seems ok over here', 'status':200, 'essay':search_essay})

''' Create essay form '''
@permission_classes([IsAuthenticated])
def form_create_essay(request, *args, **kwargs):
    if not request.user.is_authenticated:
        return render(request, 'home.html', context={'message':'Not authenticated!', 'status':401})
    else:
        _U = request.user
        FORM = EssayCreateForm(request.POST or None)
        if FORM.is_valid():
            form_data = FORM.save(commit=False)
            form_data.user = _U
            print(form_data, _U)
            form_data.save()
            return JsonResponse(FORM.data, status=201)
        if FORM.errors:
            return JsonResponse(FORM.errors, status=400)
    return render(request, 'jsys/internal_essay_create.html', context={'formName':'Create New Essay','form':FORM})
