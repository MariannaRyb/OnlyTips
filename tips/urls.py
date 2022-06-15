from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('cafes', views.index, name="all-cafes"), # list of all cafes
    path('cafes/<slug:cafe_slug>', views.cafe_waiters, name="all-waiters"), # list of all waiters
    path('waiters/<waiter_wallet>', views.waiter_details, name="about-waiter"),
    path('registration', views.registerPage, name="register-user"),
    path('login', views.loginPage, name="login"),
    path('logout', views.logoutPage, name="logout"),
    path('about', views.about, name="about"),

    path('reset_password',
         auth_views.PasswordResetView.as_view(template_name="tips/password_reset.html"),
         name="reset_password"),
    path('reset_password_sent',
         auth_views.PasswordResetDoneView.as_view(template_name="tips/password_reset_sent.html"),
         name="password_reset_done"),
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name="tips/password_reset_form.html"),
         name='password_reset_confirm'),
    path('reset_password_complete',
         auth_views.PasswordResetCompleteView.as_view(template_name="tips/password_reset_done.html"),
         name="password_reset_complete"),
    path('profile', views.profile, name='profile'),
    path('edit_profile', views.edit_profile, name='edit_profile'),
    path('edit_customer', views.edit_customer, name='edit_customer'),
    path('registration_customer', views.CustomerRegisterPage, name='register_customer'),
    path('registration_choices', views.register_choices, name='register_choices'),
    path('join', views.join, name='join'),


]
#path('waiters/<slug:cafe_slug>', views.waiter_details, name="waiter-detail")
# our-domain.com/waiters/<dynamic-path-segment>
 #keep all URLs of our app