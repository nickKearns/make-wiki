from django.urls import path, include
from accounts.views import SignupView




urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup')

]