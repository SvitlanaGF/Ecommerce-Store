from django.urls import path
from . import views
urlpatterns = [
    path('', views.cart_summary, name='cart-summary'),
    path('add', views.cart_add, name='cart-add'),
    path('update', views.cart_update, name='cart-update'),
    path('delete', views.cart_delete, name='cart-delete'),

]

# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)