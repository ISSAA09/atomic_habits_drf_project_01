from rest_framework import serializers
from habits.models import Habit
from habits.validators import SimultaneousSelectionValidator, DurationValidator, PeriodicityValidator, \
    BoundHabitValidator


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = '__all__'
        validators = [SimultaneousSelectionValidator(field1='reward', field2='bound_habit', field3='is_pleasant'),
                      DurationValidator(field='duration'), PeriodicityValidator(field='periodicity'),
                      BoundHabitValidator(field='bound_habit')]
