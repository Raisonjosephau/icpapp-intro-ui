from django.urls import path
from .views import CreateMarketView

urlpatterns = [
    path("addmarket/",CreateMarketView.as_view()),
]
