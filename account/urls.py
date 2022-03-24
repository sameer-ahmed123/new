from django.urls import path
from . import views
from .views import Index

urlpatterns = [
    path('', views.index, name= 'index'),
    path('login/', views.login_view, name='login_view'),
    path('register/', views.register, name='register'),
    path('adminpage/', views.admin, name='adminpage'),
    # path('add-shipment', views.add_shipment, name='add-shipment'),
    path('customer/', views.customer, name='customer'),
    path('add-shipment',Index.as_view(), name='add-shipment'),
    path('employee/', views.employee, name='employee'),
    path('ship-edit/<int:id>/',views.shipment_edit, name="edit"),

]