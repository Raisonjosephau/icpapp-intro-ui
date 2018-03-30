from django.urls import path
from .views import CreateUserView,vrthe,ChangePasswordView
from rest_framework_jwt.views import obtain_jwt_token


urlpatterns=[
    path('adduser/',CreateUserView.as_view(), name="adduser"),
    path('changepassword/',ChangePasswordView.as_view(), name="adduser"),
    path('login/',obtain_jwt_token, name="login"),
    path('info/',vrthe)
]