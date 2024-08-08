from django.shortcuts import render
from home.models import Contact


# Create your views here.
def home(request):
    return render(request, template_name="index.html")


def services(request):
    return render(request, template_name="services.html")


def contact(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST['email']
        phone = request.POST["phone"]
        message = request.POST["message"]
        inst_contact = Contact(name=name, email=email, phone=phone, message=message)
        inst_contact.save()
    return render(request, template_name="contact.html")


def privacyPolicy(request):
    return render(request, template_name="privacyPolicy.html")


def Tos(request):
    return render(request, template_name="Tos.html")
