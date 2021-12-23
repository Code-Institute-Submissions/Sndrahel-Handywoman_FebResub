from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm


# Code below adapted from: https://github.com/rodrigoneumann/photographer-ms4
def contact(request):
    contact_form = ContactForm()

    if request.method == "POST":
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            name = request.POST["name"]
            email = request.POST["email"]
            subject = request.POST["subject"]
            handyService = request.POST.getlist("handyService")

            services = ""
            for i in handyService:
                if i == handyService[-1]:
                    services += i
                else:
                    services += f"{i}, "

            print(handyService)
            message = request.POST["message"]
            send_mail(
                subject,
                "From: "
                + name
                + "\n\nEmail: "
                + email
                + "\n\nType of Service: "
                + services
                + "\n\nMessage: "
                + message,
                email,
                ["mocsanders@gmail.com"],
                fail_silently=False,
            )
            messages.success(
                request, "Your message was sent successfully, many Thanks!"
            )
            return redirect("contact")

    return render(request, "contact.html", {"form": contact_form})
