from django.shortcuts import render,redirect
from django.http import HttpResponse

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import views as auth_views

from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from .models import *


from django.http import Http404
import operator
import datetime

def homepage(request):
    return render(request, 'medtechapp/home.html')

def signup(request):
    if request.method=="POST":
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form=UserCreationForm()   
    return render(request, 'registration/signup.html', {
        'form':form
    }
    )  

# def logout(request):
#     return render(request, 'medtechapp/logout.html')        
@login_required
def appointment(request):
    return render(request, 'medtechapp/appointment.html')
@login_required
def homeremedies(request):
    # all_solutions=Solutions.objects.all()
    # return render(request, 'medtechapp/homeremedies.html',{'all_solutions':all_solutions})

    all_solutions=Solutions.objects.all()
    return render(request,'medtechapp/homeremedies.html',{'all_solutions': all_solutions})

    
@login_required
def organdonation(request):
    return render(request, 'medtechapp/organdonation.html')
@login_required
def map(request,newentrytable_id):
    now=datetime.datetime.now()
    try:
        newentrydata=NewEntryTable.objects.get(pk=newentrytable_id)
    except NewEntryTable.DoesNotExist:
        raise Http404("Does not exist")
    hname=request.POST.get("hname",'')
    NewEntryTable.objects.filter(id=newentrytable_id).update(hname=hname)
    print('Updated')
    t=1
    try:
        hospital=Hospital.objects.get(hospitalname=hname)
        print(hospital)
        t=hospital.token
        t=t+1
        
        Hospital.objects.filter(pk=hospital.id).update(token=t)
    # except self.model.DoesNotExist:
    except hospital.DoesNotExist:
        t=1
        newhospital=Hospital(hospitalname=hname,token=1)
        newhospital.save()
        print('Saved hospital')
        t=newhospital.token
        print('token saved')
        
    finally:
        if t==1:
            newhospital=Hospital(hospitalname=hname,token=1)
            newhospital.save()
            print('Saved hospital')
            t=newhospital.token
            print('token saved')
        time=int(t)*20
        now_plus_10=now+datetime.timedelta(minutes=time)    
            
        return render(request,'medtechapp/thankyou.html',{"token":t,'now_plus_10':now_plus_10})  


def doctormap(request):
    return render(request,'medtechapp/doctormap.html')  

def doctordisplay(request):
    dochname=request.POST.get("dochname",'')
    hospitallist=NewEntryTable.objects.all()
    hlist=[]
    for h in hospitallist:
        if dochname==h.hname:
            hlist.append(h)
    return render(request,'medtechapp/doctordisplay.html',{"hlist":hlist})           

@login_required
def thankyou(request):
    return render(request, 'medtechapp/thankyou.html') 




def newentry(request):
    fname=request.POST.get("fname",'')
    lname=request.POST.get("lname",'')
    email=request.POST.get("email",'')
    contact=request.POST.get("contact",'')
    newentrydata=NewEntryTable(fname=fname,lname=lname,email=email,contact=contact,hname="No name")
    newentrydata.save()
    print('Saved')
    return render(request,'medtechapp/map.html',{'newentrydata':newentrydata})





def orgdonation(request):
    print('updated') 
    user=request.POST.get("user",'')
    gender=request.POST.get("gender",'')
    birth=request.POST.get("birth",'')
    address=request.POST.get("address",'')
    mobile_no=request.POST.get("mobile_no",'')
    pincode=request.POST.get("pincode",'')
    organs=request.POST.get("organs",'')
    blood_group=request.POST.get("blood_group",'')
    myfile=request.POST.get("myfile",'')
    # fname=request.POST.get("fname",'')
    orgdon=DonationTable(user=user,gender=gender,birth=birth,address=address,mobile_no=mobile_no,pincode=pincode,organs=organs,blood_group=blood_group,myfile=myfile)
    orgdon.save()
    # print('final')
    return render(request,'medtechapp/donatortq.html')

 
def organ1(request):
    return render(request,'medtechapp/organ1.html')

def viewpatient(request):
    donators=DonationTable.objects.all()
    return render(request,'medtechapp/viewpatient.html',{'donators':donators})

def donatortq(request):
    return render(request,'medtechapp/donatortq')    




def request1(request):
    print("hello")
#     if request.method=='POST':
#         r_firstname=request.POST.get("f_name")
#         r_lastname=request.POST.get("l_name")
#         r_emailid=request.POST.get("email")
#         r_contact=request.POST.get("contact")


#         obj=models.request.objects.create(
#             r_firstname=r_firstname,
#             r_lastname=r_lastname,
#             r_emailid=r_emailid,
#             r_contact=r_contact,

#         )    
#         obj.save()
#         request_list=models.request.objects.all()
#         return render(request,'medtechapp/display1.html',{'request_list':request_list})
#     else:
#         return render(request,'medtechapp/homeremedies.html')

def display(request,solutions_id):
    try:
        solutions=Solutions.objects.get(pk=solutions_id)
    except Solutions.DoesNotExists:
        raise Http404("does not exits")
    return render(request,'medtechapp/display.html',{'solutions':solutions})  

    
          
@csrf_exempt
def add_hosp(request):
    print("hello form submitted")
    # print()
    # print()
    # first_name=request.POST["first_name"]
    # last_name=request.POST["last_name"]
    # email_id=request.POST["email_id"]
    # contact_number=request.POST["contact_number"]

    # user_info=UserInfo(first_name=first_name,last_name=last_name,email_id=email_id,contact_number=contact_number)
    # user_info.save()

    return render(request,'medtechapp/map.html')
       




       

# def homepage(request,*args,**kwargs):
#     if request.user.is_authenticated:
#         user = request.user
#         return render(request,'medtechapp/home.html',{'user' : user})
#     else:
#         return render(request, 'medtechapp/home.html',{})
    
        
       
       



# Create your views here.
