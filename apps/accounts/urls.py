from django.urls import path
from apps.accounts.views.organization_signup_views import OrganizationSignupView
from apps.accounts.views.login_view import LoginView
from apps.accounts.views.invite_user_view import InviteView

urlpatterns = [
    path("signup/",OrganizationSignupView.as_view(),name="organization-signup"),
    path("login/",LoginView.as_view(),name="login"),
    path("invite/",InviteView.as_view(),name="invite")
]