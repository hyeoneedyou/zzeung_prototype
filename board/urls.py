from django.urls import path
from .views import boardmain

app_name ="board"
urlpatterns = [
    path('boardmain/', boardmain, name="boardmain"),
]