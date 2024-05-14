from django.urls import path
from .views import contact_list
from . import views

urlpatterns = [
	path('contacts/', contact_list, name='contact_list'),
    path('hubspot/auth/', views.hubspot_auth, name='hubspot_auth'),
    path('hubspot/callback/', views.hubspot_callback, name='hubspot_callback'),
    path('hubspot/', views.contact_list, name='contact_list'),
    
    path('', views.home, name='home'),
    
]


