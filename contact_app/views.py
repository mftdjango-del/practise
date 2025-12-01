from django.contrib.messages import success
from django.shortcuts import render
from .models import ContactModel
from .forms import ContactForm
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

def contact_us(request):
    if request.method == "GET":
        form = ContactForm()
        return render(request, 'contact-page.html', {
            'form': form,
            'success': False
        })
    elif request.method == "POST":
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'contact-page.html', {
                'form': form,
                'success': True
            })
        else:
            return render(request, 'contact-page.html', {
                'form': form,
            })
        # full_name = request.POST.get("name")
        # image = request.FILES.get("image")
        # email = request.POST.get("email")
        # subject = request.POST.get("subject")
        # message = request.POST.get("message")
        # if len(full_name.strip()) < 1:
        #     return render(request, 'contact-page.html', {
        #         'full_name_error': True
        #     })
        # if len(email.strip()) < 6:
        #     return render(request, 'contact-page.html', {
        #         'email_error': True
        #     })
        # if len(subject.strip()) < 3:
        #     return render(request, 'contact-page.html', {
        #         'subject_error': True
        #     })
        # if len(message.strip()) < 10:
        #     return render(request, 'contact-page.html', {
        #         'message_error': True
        #     })
        # contact = ContactModel(image=image, full_name=full_name, email=email, subject=subject, message=message)
        # contact.save()
        # form = ContactForm()
        # return render(request, 'contact-page.html', {
        #     'success': True,
        #     'form': form
        # })