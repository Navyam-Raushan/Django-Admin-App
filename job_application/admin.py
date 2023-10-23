from django.contrib import admin
from .models import Form

# Register your models here.
# Here we need to register our database model

admin.site.register(Form)
# We need to create a superuser
# Run python manage.py createsuperuser

