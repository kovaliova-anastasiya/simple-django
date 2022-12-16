from django.shortcuts import render
from django.shortcuts import HttpResponse

from app.models import Message


# Create your views here.
def home(request):
    last_message = Message.objects.all().order_by('-created_at')[0]
    return HttpResponse(last_message.text)
