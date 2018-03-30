from django.urls import path
from .views import CreateUserView,vrthe


urlpatterns=[
    path('adduser/',CreateUserView.as_view(),name="adduser"),
    path('changepassword/',CreateUserView.as_view(),name="adduser"),
    path('info/',vrthe)
]