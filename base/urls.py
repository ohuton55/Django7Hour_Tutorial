from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginPage, name="login"),
    path('logiout/', views.logoutUser, name="logout"),
    path('register/', views.registerPage, name="register"),

    path('', views.home, name="home"),
    path('room_page/<str:pk>/', views.room, name="room"),
    path('profile/<str:pk>/', views.userProfile, name="user-profile"),

    path('crete_room/', views.createRoom, name="create-room"),
    path('update_room/<str:pk>/', views.updateRoom, name="update-room"),
    path('delete_room/<str:pk>/', views.deleteRoom, name="delete-room"),
    path('delete_message/<str:pk>/', views.deleteMessage, name="delete-message"),

    path('update-user/', views.updateUser, name="update-user"),
    path('topics/', views.topicPage, name="topics"),
    path('activity/', views.activityPage, name="activity"),
]