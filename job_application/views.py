from django.shortcuts import render
from .forms import ApplicationForm
from .models import Form


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
            Form.objects.create(first_name=first_name, last_name=last_name,
                                email=email, start_date=date,
                                occupation=occupation)
            print(first_name)
            print(last_name)

    return render(request, "index.html")
