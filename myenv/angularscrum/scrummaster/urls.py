from django.urls import path
from scrummaster import views

urlpatterns = [
    path('users/', views.user_list),
    path('user/<int:pk>/', views.user_detail),
    path('goals/', views.scrumy_goals_list),
    path('goals/<int:pk>/', views.scrumy_goal_detail),

]