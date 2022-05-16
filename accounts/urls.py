from django.urls import path

from accounts import views

app_name = 'accounts'

urlpatterns = [
    path('sign-up', views.account_sign_up, name='account_sign_up'),
    path('sign-in', views.account_sign_in, name='account_sign_in'),
    path('account-info/<slug:slug>', views.account_info, name='account_info'),
]
