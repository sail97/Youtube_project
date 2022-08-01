from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import auth,messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth import logout
# Create your views here.

def login(request):
    if request.method == 'POST':
        userName=request.POST['userName']
        password=request.POST['password']
        user = auth.authenticate(username=userName , password=password)
        print(userName,password)
        if user is not None:
            auth.login(request,user)
            messages.success(request,'successfully logged in')
            return redirect('dashboard')
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')

    return render(request, 'accounts/login.html')

def register(request):
    if request.method == 'POST':
        firstName = request.POST['firstName']
        lastName = request.POST['lastName']
        userName = request.POST['userName']
        email = request.POST['email']
        password = request.POST['password']
        confirmPassword = request.POST['confirmPassword']

        if password == confirmPassword:
            if len(password)>6 or len(password)<20:
                if User.objects.filter(username = userName).exists():
                    messages.info(request,"user already exists")
                    return redirect('register')
                else:
                    user = User.objects.create_user(first_name=firstName,last_name=lastName,username=userName,email=email,password=password)
                    user.save()
                    messages.success(request,"user created succcessfully")
                    return redirect('login')
            else:
                print("password should be minimum 6 characters")
        else:
            messages.info(request,'passwords do not match')
            return redirect('register')


    return render(request,'accounts/register.html')

def logout_user(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def dashboard(request):
    return render(request,'accounts/dashboard.html')