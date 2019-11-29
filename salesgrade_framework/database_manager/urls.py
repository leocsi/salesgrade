from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:user_age>', views.same_age, name='same_age'),
    path('<str:user_name>',views.own_results, name='own_results')
]