from django.urls import path
from . import views
urlpatterns = [
    path('index/', views.index),
    path('home/', views.index),
    path('', views.index),
    path('about/', views.about),
    path('contact/', views.contact),
    path('login/', views.login),
    path('signin/', views.signin),
    path('gallery/', views.gallery),
    path('myassignment/', views.myassignment),
    path('assignmentdetails/', views.assignmentdetails),
    path('logout/', views.logout),
    path('profile/', views.profile),
    path('lectures/', views.lectures),
    path('lcategory/', views.lcategory),
    path('viewlecture/', views.viewlecture),
    path('developer/', views.developer),
]