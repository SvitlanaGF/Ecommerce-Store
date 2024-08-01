from django.urls import path, include
from . import views
urlpatterns = [
    path('register', views.register, name='register'),
    path('email-verification/<str:uidb64>/<str:token>/', views.email_verification, name='email_verification'),
    path('email-verification-success', views.email_verification_success, name='email_verification_success'),
    path('email-verificstion-failed', views.email_verification_failed, name='email_verification_failed'),
    path('email-verification-sent', views.email_verification_sent, name='email_verification_sent'),
    path('my-login', views.my_login, name='my_login'),
    path('dashboard', views.dashboard, name='dashboard'),
]

# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)