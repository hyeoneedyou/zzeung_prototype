from django.urls import path
from .views import main, first, second, third, review, review2, create, create2, show, update, delete


app_name ="accounting"
urlpatterns = [
    path('', main, name="main"),
    path('first/', first, name="first"),
    path('second/', second, name="second"),
    path('third/', third, name="third"),
    path('review/', review, name="review"),
    path('review2/', review2, name="review2"),
    path('create/', create, name="create"),
    path('create2/', create2, name="create2"),
    path('show/<int:id>', show, name="show"),
    path('update/<int:id>/', update, name="update"),
    path('delete/<int:id>/', delete, name="delete"),
]