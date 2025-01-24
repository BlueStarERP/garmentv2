from django.shortcuts import render,redirect,get_object_or_404,HttpResponse

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib import messages
from .forms import *
from .models import *
# Create your views here.
def loginpage(request):
    if request.user.is_authenticated:
        return redirect('account:home')
    else:
        if request.method == "POST":
            username=request.POST.get('username')
            password=request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('account:home')
            else:
                messages.info(request, 'username or password invalid')
            # return render(request, 'login.html', context)
        context ={}
        return render(request, 'login.html', context)
    

def logoutuser(request):
    logout(request)
    return redirect('account:login')

def registerpage(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            # messages.success(request, 'User Created Successful')
            return redirect('account:login')
    context ={'form':form}
    return render(request, 'register.html', context)


@login_required(login_url='account:login')
def createcompany(request):
    form = CreateCompanyForm()
    if request.method == "POST":
        company_name=request.POST.get('company_name')
        phone=request.POST.get('phone')
        address=request.POST.get('address')
        profile = CompanyProfile.objects.create(company_name=company_name, phone=phone, address=address, user=request.user)
        per = StaffPermission.objects.create(usr=request.user,company=profile)
        return redirect('account:home')
    context ={'form':form}
    return render(request, 'companyprofile.html', context)


@login_required(login_url='account:login')
def home(request):
    try:
        # p = CompanyProfile.objects.get(user=request.user)
        p = StaffPermission.objects.get(usr = request.user)
        # print(p.hr)
        if p.manager is True:
            return render(request, 'home.html')
        elif p.qc is True:
            print('QC')
        elif p.admin is True:
            print('Admin')
        elif p.supervisor is True:
            print('Supervisor')
        

        return render(request, 'home.html')
    except StaffPermission.DoesNotExist:
        # return HttpResponse('hellllo')
        return redirect('account:createcompany')


@login_required(login_url='account:login')
def createstaffaccount(request):
    try:
        company_obj = CompanyProfile.objects.get(user=request.user)
        form = CreateUserForm()
        per = StaffPermission.objects.filter(company=company_obj)
        context = {'company_obj':company_obj, 'per':per, 'form':form}
        return render(request, 'createstaffaccount.html', context)
    except CompanyProfile.DoesNotExist:
        return redirect('account:login')

def reguseraccount(request):
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            a = form.instance.id
            user_obj = User.objects.get(id=a)
            company_obj = CompanyProfile.objects.get(user=request.user)
            per = StaffPermission.objects.create(usr=user_obj,company=company_obj)
            # print(a)
    
    return redirect("account:createstaffaccount")
    # return JsonResponse({'status':'success'})
    


 

# update view for details
def user_update_view(request, id):
    # dictionary for initial data with 
    # field names as keys
    context ={}
 
    # fetch the object related to passed id
    obj = get_object_or_404(StaffPermission, id = id)
 
    # pass the object as instance in form
    form = StaffPermissionForm(request.POST or None, instance = obj)
 
    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return redirect("account:createstaffaccount")
 
    # add form dictionary to context
    context["form"] = form
 
    return render(request, "user_update_view.html", context)


def line_setup(request):
    line = LineName.objects.all()
    context ={}
    return render(request, "line_setup.html", context)