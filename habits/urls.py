from django.urls import path
from habits.apps import HabitsConfig
from habits.views import (
    HabitCreateAPIView, 
    HabitListAPIView, 
    HabitRetrieveAPIView, 
    HabitUpdateAPIView, 
    HabitDestroyAPIView,
    HabitPublishedListAPIView
)

app_name = HabitsConfig.name


urlpatterns = [
    path('habits/create/', HabitCreateAPIView.as_view(), name='habit_create'),
    path('', HabitListAPIView.as_view(), name='habit_list'),
    path('published/', HabitPublishedListAPIView.as_view(), name='published_list'),
    path('habits/<int:pk>/', HabitRetrieveAPIView.as_view(), name='habit_detail'),
    path('habits/<int:pk>/update/', HabitUpdateAPIView.as_view(), name='habit_update'),
    path('habits/<int:pk>/delete/', HabitDestroyAPIView.as_view(), name='habit_detete'),
]
