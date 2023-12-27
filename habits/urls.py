from django.urls import path
from habits.apps import HabitsConfig
from habits.views import HabitCreateAPIView, HabitUpdateAPIView, HabitDestroyAPIView, PublicHabitListAPIView, \
    HabitListAPIView

app_name = HabitsConfig.name

urlpatterns = [
    path('habit/create/', HabitCreateAPIView.as_view(), name='habit_create'),
    path('habit/update/<int:pk>/', HabitUpdateAPIView.as_view(), name='habit_update'),
    path('habit/delete/<int:pk>/', HabitDestroyAPIView.as_view(), name='habit_delete'),
    path('habit/list/public/', PublicHabitListAPIView.as_view(), name='habit_list_public'),
    path('habit/list/', HabitListAPIView.as_view(), name='habit_list'),
]
