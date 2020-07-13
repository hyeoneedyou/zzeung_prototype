from django.urls import path
from .views import list, first, second, third, review, create, show


app_name ="accounting"
urlpatterns = [
    path('list/', list, name="list"),
    path('first/', first, name="first"),
    path('second/', second, name="second"),
    path('third/', third, name="third"),
    path('review/', review, name="review"),
    path('create/', create, name="create"),
    path('/show/<int:id>', show, name="show"),
]