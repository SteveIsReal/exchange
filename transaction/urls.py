from django.urls import path
from transaction import views

urlpatterns = [
    path('exchange/', views.Exchange.as_view()),
    path('login/', views.Login.as_view())

]
