from django.urls import path
from transaction import views

urlpatterns = [
    path('exchange/', views.exchange.as_view())

]