from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('deals/', views.deals, name='deals'),
    path('leads/', views.leads, name='leads'),
    path('get_lead/', views.get_lead, name='get_lead'),
    path('get_deal/', views.get_deal, name='get_deal'),
    path('delete_lead/', views.delete_lead, name='delete_lead'),
    path('delete_deal/', views.delete_deal, name='delete_deal'),
]
