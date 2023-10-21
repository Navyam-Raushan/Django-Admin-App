from django.shortcuts import render
from .forms import ApplicationForm
from .models import Form
from django.contrib import messages
from django.core.mail import EmailMessage


# Create your views here.
# Here we will create our pages (views)
# No need to call the function just declare.

def index(request):
    if request.method == "POST":
        form = ApplicationForm(request.POST)

        if form.is_valid():
            # Format is somewhat form.cleaned_data["name given in html"]
            # print(form.cleaned_data)
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            email = form.cleaned_data["email"]
            date = form.cleaned_data["date"]
            occupation = form.cleaned_data["occupation"]

            # Adding values to the database.
            Form.objects.create(first_name=first_name, last_name=last_name,
                                email=email, start_date=date,
                                occupation=occupation)
            print(first_name)
            print(last_name)

            # Sending Email

            # Format for EmailMessage class
            # send_mail(
            #     'Subject here',
            #     'Here is the message.',
            #     'from@example.com',
            #     ['to@example.com'],
            #     fail_silently=False,
            # )
            body = f"{first_name}, Thanks for showing interest \n" \
                   f"We received your Application Form.\n" \
                   f"Thanks."
            email_message = EmailMessage("Form submission confirmation",
                                         body=body, to=[email]
                                         )

            email_message.send()

            # Displaying messages from django.messages (green color is due to
            messages.success(request, message="Form is submitted successfully")

    return render(request, "index.html")
