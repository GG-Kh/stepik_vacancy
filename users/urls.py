from django.urls import path
from django.contrib.auth.views import LogoutView

from users import views


urlpatterns = [
    path('login/', views.MyLoginView.as_view(), name='login'),
    path('signup/', views.SignupView.as_view(), name='signup'),
    path('logout/', LogoutView.as_view(), name='logout')
]
