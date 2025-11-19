from django.urls import path
from apps.accounts.views.organization_signup_views import OrganizationSignupView

urlpatterns = [
    path("signup/",OrganizationSignupView.as_view(),name="organization-signup")
]