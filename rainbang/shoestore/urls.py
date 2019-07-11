from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:shoe_id>/', views.shoe, name='shoe'),
]
