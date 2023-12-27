from rest_framework.serializers import ValidationError


class SimultaneousSelectionValidator:
    def __init__(self, field1, field2, field3):
        self.field1 = field1
        self.field2 = field2
        self.field3 = field3

    def __call__(self, val):
        field1 = dict(val).get(self.field1)  # Вознаграждение
        field2 = dict(val).get(self.field2)  # Связанная привычка
        field3 = dict(val).get(self.field3)  # Признак приятной привычки
        if field1 is None and field2 is None and field3 is False:
            raise ValidationError("You must fill out one of two fields (Reward or Bound habit")
        elif field1 and field2:
            raise ValidationError("Cannot choose both reward and bound habit at the same time")
        elif field3 is True and field1 or field3 is True and field2:
            raise ValidationError("A pleasant habit cannot have a reward or a bound habit'")


class DurationValidator:

    def __init__(self, field):
        self.field = field

    def __call__(self, val):
        field = dict(val).get(self.field)
        if field is not None and field > 120 or field and field > 120:
            raise ValidationError("Duration should be less 120 sec")


class PeriodicityValidator:

    def __init__(self, field):
        self.field = field

    def __call__(self, val):
        field = dict(val).get(self.field)
        if field is not None and field > 7 or field and field > 7:
            raise ValidationError("Periodicity should be not more 7 days")


class BoundHabitValidator:

    def __init__(self, field):
        self.field = field

    def __call__(self, val):
        field = dict(val).get(self.field)
        if field is not None and not field.is_pleasant or field and not field.is_pleasant:
            raise ValidationError("Only pleasant habits can be chosen as bound habits")
