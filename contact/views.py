# Create your views here.
# Create your views here.
from django.shortcuts import render, redirect
from .models import Contact

def home(request):
    if request.method == "POST":
        Contact.objects.create(
            name=request.POST.get("name"),
            email=request.POST.get("email"),
            message=request.POST.get("message")
        )
        return redirect("/")

    contacts = Contact.objects.all()

    return render(request, "index.html", {
        "contacts": contacts
    })


def delete_contact(request, id):
    contact = Contact.objects.get(id=id)
    contact.delete()
    return redirect("/")

def edit_contact(request, id):
    contact = Contact.objects.get(id=id)

    if request.method == "POST":
        contact.name = request.POST.get("name")
        contact.email = request.POST.get("email")
        contact.message = request.POST.get("message")
        contact.save()
        return redirect("/")

    return render(request, "edit.html", {"contact": contact})
