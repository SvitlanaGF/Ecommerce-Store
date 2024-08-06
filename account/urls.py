from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('register', views.register, name='register'),
    path('email-verification/<str:uidb64>/<str:token>/', views.email_verification, name='email_verification'),
    path('email-verification-success', views.email_verification_success, name='email_verification_success'),
    path('email-verificstion-failed', views.email_verification_failed, name='email_verification_failed'),
    path('email-verification-sent', views.email_verification_sent, name='email_verification_sent'),
    path('my-login', views.my_login, name='my_login'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('user-logout', views.user_logout, name='user_logout'),
    path('manage-profile', views.profile_update, name='manage_profile'),
    path('delete-profile', views.delete_profile, name='delete_profile'),
    # path('change-password', auth_views.PasswordChangeView.as_view(), name='change_password'),
    path('reset-password', auth_views.PasswordResetView.as_view(template_name='account/password/password-reset.html'), name='password_reset'),
    path('reset-password-done', auth_views.PasswordResetDoneView.as_view(template_name='account/password/password-reset-sent.html'), name='password_reset_done'),
    path('reset/<uid64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='account/password/password-reset-form.html'), name='password_reset_confirm'),
    path('reset-password-complete', auth_views.PasswordResetCompleteView.as_view(template_name='account/password/password-reset-complete.html'), name='password_reset_complete'),

]

