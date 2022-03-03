from django.urls import path

from home import views 

urlpatterns=[
    path('', views.index, name='home'),

    path('index', views.index, name='index'),

    path('menu',views.menu, name='menu'),

    path('offers',views.offers, name='offers'),
]
