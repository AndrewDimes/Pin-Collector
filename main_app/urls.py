from django.urls import path
from . import views     

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('pins/', views.pins_index, name='index'),
    path('pins/<int:pin_id>/', views.pins_detail, name='detail'),
    path('pins/create/', views.PinCreate.as_view(), name='pins_create'),
    path('pins/<int:pk>/update/', views.PinUpdate.as_view(), name='pins_update'),
    path('pins/<int:pk>/delete/', views.PinDelete.as_view(), name='pins_delete'),
]