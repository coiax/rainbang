from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:shoe_id>/', views.shoe, name='shoe'),
    path('<int:shoe_id>/<int:style_id>/', views.shoe_with_style, name='shoe_with_style'),
]
