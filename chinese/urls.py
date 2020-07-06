from django.urls import path
from .views import list, first, second, third

app_name ="chinese"
urlpatterns = [
    path('list/', list, name="list"),
    path('first/', first, name="first"),
    path('second/', second, name="second"),
    path('third/', third, name="third"),
]