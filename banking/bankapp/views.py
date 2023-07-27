from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import District, Branch


# Create your views here.
def home(request):
    return render(request, "index.html")


def register(request):
    if request.method == 'POST':
        uname = request.POST['username']
        password = request.POST['password']
        cpass = request.POST['cpassword']
        if password == cpass:
            if User.objects.filter(username=uname).exists():
                messages.info(request, "Username is Taken")
                return redirect("bankapp:register")
            else:
                user = User.objects.create_user(username=uname, password=password)
                user.save();
                return redirect('bankapp:login')
        else:
            messages.info(request, "Password not Matching")
            return redirect('bankapp:register')
    return render(request, "register.html")


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('bankapp:form')
        else:
            messages.info(request, "Invalid Credentials")
            return redirect('bankapp:login')
    return render(request, "login.html")


def form(request, form=None):
    distdata = District.objects.all()
    branchdata = Branch.objects.all()
    if request.method == 'POST':
        name = request.POST['name']
        dob = request.POST['dob']
        age = request.POST['age']
        gender = request.POST['gender']
        phone = request.POST['phone']
        email = request.POST['email']
        address = request.POST['address']
        district = request.POST['district']
        branch = request.POST['branch']
        account = request.POST['acc']
        material = request.POST['material']
        form = form.objects.create_form(name=name, dob=dob, age=age, gender=gender, phone=phone, email=email,
                                        address=address,
                                        district=district, branch=branch, account=account, material=material)
        form.save();
        return redirect('/')
    return render(request, "form.html", {'dist': distdata, 'bran': branchdata})


def logout(request):
    auth.logout(request)
    return redirect('/')



