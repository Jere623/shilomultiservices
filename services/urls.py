from django.urls import path
from . import views
urlpatterns=[path('',views.home,name='home'),path('devis/',views.quote,name='quote'),path('contact/',views.contact,name='contact'),path('services/<int:pk>/',views.detail,name='detail')]
