# views.py

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Notification
from Login_Logout.models import User


from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator




def mark_notifications_as_read(request):
    request.user.notifications.filter(is_read=False).update(is_read=True)
    return JsonResponse({'status': 'success'})

