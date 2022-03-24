from django.shortcuts import render, redirect
from .forms import SignUpForm, LoginForm
from .models import Shipment
from django.contrib.auth import authenticate, login
# Create your views here.
from django.views import View
from account.models import Shipment
#from account.forms import ShipmentForm


def index(request):
    return render(request, 'index.html')

# def add_shipment(request):
#     if request.method == "POST":
#         form = ShipmentForm(request.POST)
#         if form.is_valid():
#             try:
#                 form.save()
#                 return redirect('customer')
#             except:
#                 pass
#     else:
#         form = ShipmentForm()
#     print("form is:",form)
#     return render(request,'customer.html',{'form':form})


def register(request):
    msg = None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            msg = 'user created'
            return redirect('login_view')
        else:
            msg = 'form is not valid'
    else:
        form = SignUpForm()
    return render(request,'register.html', {'form': form, 'msg': msg})

# def shipment(request):
#     msg = None
#     if request.method == 'POST':
#         form = ShipmentForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             msg = 'Shipment Created'
#             return redirect('login_view')
#         else:
#             msg = 'form is not valid'
#     else:
#         form = ShipmentForm()
#     print("Form is:",form)
#     return render(request,'add-shipment.html', {'form': form, 'msg': msg})



def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_admin:
                login(request, user)
                return redirect('adminpage')
            elif user is not None and user.is_customer:
                login(request, user)
                # return redirect('add-shipment')
                return redirect('add-shipment')
            elif user is not None and user.is_employee:
                login(request, user)
                return redirect('employee')
            else:
                msg= 'invalid credentials'
        else:
            msg = 'error validating form'
    return render(request, 'login.html', {'form': form, 'msg': msg})


# def save_shipment(request):
#     msg = None
#     if request.method == 'POST':
#         form = ShipmentForm(request.POST)
#         if form.is_valid():
#             saveForm = form.save(commit=False)
#             saveForm.user = request.user
#             if 'status' in request.POST:
#                 Shipment.objects.update(status=False)
#             saveForm.save()
#             msg = "Shipment has been saved"
#     form = ShipmentForm
#     return render(request, 'customer.html',{'form':form,'msg':msg})



def admin(request):
    return render(request,'admin.html')


def customer(request):
    return render(request,'customer.html')


def employee(request):
    ship = Shipment.objects.all()
    return render(request,'employee.html', {"ship": ship})

def shipment_edit(request, id ):
    form = SignUpForm()
    edt = Shipment.objects.get(id=id)
    options = Shipment.objects.all()
    print(options)
    return render(request, "edit.html", {"edt": edt, "options": options, "form": form})

class Index(View):

    def get(self, request):
        return render(request,'add-shipment.html')

    def post(self,request):
        postData = request.POST
        pickupTime = postData.get('pickupTime')
        userLocation = postData.get('userLocation')
        NoOfBoxes = postData.get('NoOfBoxes')
        recieverLocation = postData.get('recieverLocation')
        recievername = postData.get('recievername')
        recieverphone = postData.get('recieverphone')
        # status = postData.get('status')

        data = {
            'pickupTime': pickupTime,
            'userLocation': userLocation,
            'NoOfBoxes': NoOfBoxes,
            'recieverLocation': recieverLocation,
            'recievername': recievername,
            'recieverphone': recieverphone,
            # 'status': status
        }

        add_shipment = Shipment(pickupTime=pickupTime,
                                   userLocation=userLocation,
                                   NoOfBoxes=NoOfBoxes,
                                   recieverLocation=recieverLocation,
                                   recievername=recievername,
                                   recieverphone=recieverphone,
                                   # status=status

                                   )
        add_shipment.save()
        print("Data is:",add_shipment)
        return redirect('add-shipment')