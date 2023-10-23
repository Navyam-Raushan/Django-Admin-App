from django.urls import path
from . import views

# Here we will add all the urls of our page.
# format is like path('directory', callback_function, name="same name as function")
# Don't do typos variable name must be urlpatterns.
urlpatterns = [
    path('', views.index, name="index"),
    path("about/", views.about, name="about")
]
