from django.urls import path
from .views import main, first, second, third

app_name ="computer"
urlpatterns = [
    path('', main, name="main"),
    path('first/', first, name="first"),
    path('second/', second, name="second"),
    path('third/', third, name="third"),
]