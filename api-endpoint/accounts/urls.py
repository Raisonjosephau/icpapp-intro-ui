from django.urls import path
from .views import CreateUserView,vrthe
from rest_framework_jwt.views import obtain_jwt_token


urlpatterns=[
    path('adduser/',CreateUserView.as_view(), name="adduser"),
    path('changepassword/',CreateUserView.as_view(), name="adduser"),
    path('login/',obtain_jwt_token, name="login"),
    path('info/',vrthe)
]