from django.db import models


# Create your models here (db models)
# Just create this model connection with dbms (django will do it)
class Form(models.Model):
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    email = models.EmailField()
    start_date = models.DateField()
    occupation = models.CharField(max_length=80)

    # __str__ function prints returned statement when we print this class.
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

