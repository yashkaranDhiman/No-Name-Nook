from django.urls import path
from home import views

urlpatterns = [
    path("",views.index,name="homepage"),
    path("room<int:pk>/",views.enter_room,name="roompage"),
    path('<int:room_id>/add_message/', views.addMessage, name='add_message'),
]
