from django.contrib import admin
from .models import Form


# Register your models here.
# Here we need to register our database model

class FormAdmin(admin.ModelAdmin):
    # Just define some previously defined variables to alter interface
    # field name should be same as declared in db model

    # list_display will show these info on home page.
    list_display = ("first_name", "last_name", "email")

    # search_field will search any entry based on these fields
    search_fields = ("first_name", "last_name", "email")

    # list_filter will filter the entry based on those fields
    list_filter = ("start_date", "occupation")

    # ordering means sorting basis on that field (for reverse put - sign)
    ordering = ("-first_name",)

    # to make any field read only
    readonly_fields = ("occupation", "start_date")


admin.site.register(Form, FormAdmin)
# We need to create a superuser
# Run python manage.py createsuperuser
