# website/views.py

from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from .forms import ContactForm

def home(request):
    form = ContactForm()
    menu_items = ["home", "about", "skills", "projects", "experience", "education", "contact"]

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            sender = form.cleaned_data['email']
            msg = form.cleaned_data['message']

            subject = f"Portfolio Contact: {name}"
            full_message = f"{msg}\n\nFrom: {name} <{sender}>"

            # Email to yourself
            send_mail(
                subject,
                full_message,
                settings.EMAIL_HOST_USER,
                [settings.EMAIL_HOST_USER, 'raisurjaprdp@gmail.com'],
                fail_silently=False,
            )

            # Auto reply to sender
            send_mail(
                "Thanks for contacting me!",
                f"Hi {name},\n\nThanks for your message. I'll be in touch soon!",
                settings.EMAIL_HOST_USER,
                [sender],
                fail_silently=False
            )

            messages.success(request, "✅ Your message was sent successfully!")
            return redirect('/#contact')


    return render(request, 'website/index.html', {
        'form': form,
        'menu_items': menu_items,
    })
