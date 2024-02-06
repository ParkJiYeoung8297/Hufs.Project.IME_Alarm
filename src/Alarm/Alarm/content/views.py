from django.shortcuts import render
from rest_framework.views import APIView
from .models import Post


# Create your views here.
class NewAlarm(APIView):
    def get(self,request):
        return render(request,"content/alarm.html")
    
    