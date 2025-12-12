from django.shortcuts import render,redirect,HttpResponse
from django.template import RequestContext
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as auth_login
from . models import *
# Create your views here.
def home(request):
    return render(request,"home.html")

def register(request):
    if request.method == "POST":
        first_name=request.POST.get("fname",None)
        last_name=request.POST.get("lname",None)
        email=request.POST.get("email",None)
        mobile_number=request.POST.get("mnumber",None)
        password=request.POST.get("password",None)
        address=request.POST.get("address",None)
        user=User.objects.create_user(username=email,email=email,first_name=first_name,last_name=last_name,password=password,)
        return redirect("login")
    return render(request,"register.html")

def login(request):
    if request.method == "POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        user=authenticate(request,**{"username":username,"password":password})
        print(user)
        if not (user):
            print("user not found,please register")
        else:
            print("user found, logged in")

            auth_login(request,user)
            print(request.user)
            return redirect("create_invoice")


    return render(request,"login.html")


def create_invoice(request):
    if request.method == "POST":
        invoice_date=request.POST.get("invoice_date") or None
        invoice_number=request.POST.get("invoice_number") or None
        customer_name=request.POST.get("customer_name")
        due_date=request.POST.get("due_date")
        product_name=request.POST.get("product_name")
        qty=request.POST.get("qty")
        rate=request.POST.get("rate")
        total=request.POST.get("total")
        Invoice.objects.create(invoice_date=invoice_date,invoice_number=invoice_number,customer_name=customer_name,due_date=due_date,qty=qty,rate=rate,total=total,user=request.user)

        return redirect("viewinvoice")
    return render(request, "invoice.html")

def viewinvoice(request):
    invoices=Invoice.objects.all()
    context={"invoice1":invoices}
    print(invoices.first())
    
    return render(request, "viewinvoice.html",context)

def deleteinvoice(request,pk):
    Invoice.objects.filter(id=pk).delete()
    invoices=Invoice.objects.all()
    context={"invoice1":invoices}
    
    return render(request,"viewinvoice.html",context)

