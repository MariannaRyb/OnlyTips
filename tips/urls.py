from django.urls import path
from . import views

urlpatterns = [
    path('cafes', views.index, name="all-cafes"), # list of all cafes
    path('cafes/<slug:cafe_slug>', views.cafe_waiters, name="all-waiters"), # list of all waiters
    path('waiters/<waiter_wallet>', views.waiter_details, name="about-waiter"),
    path('registration', views.registerPage, name="register-user"),
    path('login', views.loginPage, name="login")]
#path('waiters/<slug:cafe_slug>', views.waiter_details, name="waiter-detail")
# our-domain.com/waiters/<dynamic-path-segment>
 #keep all URLs of our app