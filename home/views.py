from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def index(request):
    context = {
        "variable1":"This website is Great because it is made by Mohammed Umar Hahahaha",
        "variable2":"Umar is Greate"
    }
    # messages.success(request, "this is a test message")
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')
    # return HttpResponse("This is About Page")

def services(request):
    return render(request, 'services.html')

@csrf_exempt
def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent!')
    
    return render(request, 'contact.html')


def projects(request):
    return render(request, 'projects.html')
    