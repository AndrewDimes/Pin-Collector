from django.urls import path
from . import views     

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('pins/', views.pins_index, name='index'),
    path('pins/<int:pin_id>/', views.pins_detail, name='detail')
]