from django.shortcuts import redirect, render
from .models import Hiretuber
from django.contrib import messages
# Create your views here.

def hiretuber(request):
    if request.methos == 'POST':
        fname=request.POST['fname']
        lname=request.POST['lname']
        user_id=request.POST['user_id']
        email=request.POST['email']
        tuber_name=request.POST['tuber_name']
        city=request.POST['city']
        state=request.POST['state']
        phone=request.POST['phone']
        message=request.POST['message']
        ytuber_id=request.POST['ytuber_id']


        hiretuber = Hiretuber(first_name = fname, last_name=lname, tuber_id = ytuber_id,  user_id = user_id, email = email, tuber_name = tuber_name, city = city, state = state, phone = phone, message = message)
        hiretuber.save()
        messages.success(request, "thanks for reaching out")
        return redirect('youtubers')