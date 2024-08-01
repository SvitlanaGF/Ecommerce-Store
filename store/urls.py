from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='store'),
    path('product/<slug:slug>/', views.product, name='product-info'),
    path('search/<slug:category_slug>/', views.list_category, name='list-category'),
]
