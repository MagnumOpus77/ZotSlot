from django.urls import path
from . import views

# from .views import RoomView

# urlpatterns = [
#     path("", RoomView.as_view())      # if we get a blank url, call the main function
# ]

urlpatterns = [
    #path("<int:id>"), view.index, name="index"),
    path("<str:name>", views.index, name="index"),
    path("", views.create, name="create"),
]