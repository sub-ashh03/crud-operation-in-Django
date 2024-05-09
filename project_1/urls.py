from django.urls import path
from .views import *

urlpatterns = [
    path ('', homepage),
    path('add_product/', ADD_form_2),
    path('insert/', insertData),
    path('update/<id>', updateData),
    path('delete/<id>', deleteData),
]