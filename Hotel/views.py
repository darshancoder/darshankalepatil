from django.shortcuts import render 
from django.http import HttpResponse, HttpResponseRedirect
from Hotel.models import Customer
from Hotel.models import Contact
from .forms import CustomerRegistration

# Create your views here.restaurant(request):


def restaurant(request):
      return render(request, 'Hotel/homepage.html')


def customerinfo(request):
      cust = Customer.objects.all()
      return render (request, 'Hotel/customerinfo.html', {'cus':cust})


def thankyou(request):
      return render (request, 'Hotel/success.html')


def showformdata(request):
      # fm = CustomerRegistration()
      # return render (request, 'Hotel/homepage.html', {'form':fm})


      if request.method == "POST":
            fm = CustomerRegistration(request.POST)
            if fm.is_valid():
                  print("Form is validated")
                  print("Name:", fm.cleaned_data['name'])
                  print("Email:", fm.cleaned_data['email'])
                  return HttpResponseRedirect('/Hotel/success/')

      else:
            fm = CustomerRegistration()
            print("Form is not validated")
      return render(request, 'Hotel/homepage.html', {'Form':fm})


def info(request):
      if request.method == "POST":
            name=request.POST.get('name')
            email=request.POST.get('email')
            subject=request.POST.get('subject')
            message=request.POST.get('message')
            fm= Contact(name=pname, email=email , subject=psubject , message= pmessage)
            fm.save()
      return render(request,'Hotel/homepage.HTML')            




