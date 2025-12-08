from django.urls import path
from apps.accounts.views.organization_signup_views import OrganizationSignupView
from apps.accounts.views.login_view import LoginView
from apps.accounts.views.invite_user_view import InviteView
from apps.accounts.views.invite_user_view import AcceptInviteView

urlpatterns = [
    path("signup/",OrganizationSignupView.as_view(),name="organization-signup"),
    path("login/",LoginView.as_view(),name="login"),
    path("invite/",InviteView.as_view(),name="invite"),
    path("accept-invite/<str:token>/", AcceptInviteView.as_view())
]