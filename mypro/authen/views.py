from django.shortcuts import render,redirect
from django.contrib.auth.models import User     # it predefined in database so we import in views
from django.contrib.auth import authenticate,login,logout      # for (login) matching the user_data,here authenticate is a function

# Create your views here.

def login_(request):
    login_nav = True
    if request.method=='POST':
        username_data=request.POST['username']
        password_data=request.POST['password']
        print(username_data,password_data)
        user=authenticate(username=username_data,password=password_data) # for matching the details
        print(user)    # if data is not match it will return None
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return render(request,'wrong.html')
    return render(request,'login.html', context={'login_nav':login_nav})

def register(request):
    login_nav = True
    if request.method == 'POST':
        firstname_data = request.POST['firstname']
        lastname_data = request.POST['lastname']
        email_data = request.POST['email']
        username_data = request.POST['username']
        password_data = request.POST['password']
        user = User.objects.create(first_name=firstname_data, last_name=lastname_data,email=email_data, username=username_data)
        user.set_password(password_data)
        user.save() 
        return redirect('login')
    return render(request, 'reg.html', context={'login_nav':login_nav})


def logout_(request):
    logout(request)
    return redirect('login')

def profile(request):
    return render(request,'profile.html')

    