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
    path('pins/<int:pin_id>/add_comment/', views.add_comment, name='add_comment'),
    path('categories/', views.CategoryList.as_view(), name='categories_index'),
    path('categories/<int:category_id>/', views.categories_detail, name='categories_detail'),
    path('categories/create/', views.CategoryCreate.as_view(), name='categories_create'),
    path('categories/<int:pk>/update/', views.CategoryUpdate.as_view(), name='categories_update'),
    path('categories/<int:pk>/delete/', views.CategoryDelete.as_view(), name='categories_delete'),
    path('categories/<int:category_id>/assoc_pin/<int:pin_id>/', views.assoc_pin, name='assoc_pin'),
]