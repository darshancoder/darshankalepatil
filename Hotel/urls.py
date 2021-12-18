
from django.urls import path
from . import views

urlpatterns = [
      path('home/',views.restaurant),
      path('info/', views.customerinfo),
      path('form/', views.showformdata),
      path('success/', views.thankyou, name = "success"),
      path('message',views.info,name ='info'),
   

    

]