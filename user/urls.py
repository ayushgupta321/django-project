from django.urls import path
from . import views


urlpatterns = [
    path('',views.index,name='index'),
    path('form_page.html/',views.formrequest),
]