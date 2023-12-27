from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from habits.models import Habit
from users.models import User


class HabitTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(
            email='iska29@inbox.ru',
            password='test',
            is_active=True,
            is_staff=True,
            is_superuser=True,
        )
        self.client.force_authenticate(user=self.user)

        self.first_habit = Habit.objects.create(time="11:00", action="test action 1", duration=50, is_pleasant=False,
                                                periodicity=1, is_public=True, reward="test reward 1",
                                                place='Home', user=self.user)

        self.second_habit = Habit.objects.create(time="13:00", action="test action 2", duration=80, is_pleasant=False,
                                                 periodicity=1, is_public=True, reward="test reward 2",
                                                 place='Home_2', user=self.user)

    def test_list_my_habit(self):
        response = self.client.get(
            reverse('habits:habit_list')
        )

        self.assertEquals(response.status_code, status.HTTP_200_OK)
        print(response.json())
        self.assertEquals(response.json(), {
            "count": 2,
            "next": None,
            "previous": None,
            "results": [
                {
                    "id": self.first_habit.pk,
                    "bound_habit": self.first_habit.bound_habit,
                    "periodicity": self.first_habit.periodicity,
                    "duration": self.first_habit.duration,
                    "time": "11:00:00",
                    "action": self.first_habit.action,
                    "reward": self.first_habit.reward,
                    "is_pleasant": self.first_habit.is_pleasant,
                    "is_public": self.first_habit.is_public,
                    "user": self.first_habit.user.pk,
                    "place": self.first_habit.place
                },
                {
                    "id": self.second_habit.pk,
                    "bound_habit": self.second_habit.bound_habit,
                    "periodicity": self.second_habit.periodicity,
                    "duration": self.second_habit.duration,
                    "time": "13:00:00",
                    "action": self.second_habit.action,
                    "reward": self.second_habit.reward,
                    "is_pleasant": self.second_habit.is_pleasant,
                    "is_public": self.second_habit.is_public,
                    "user": self.second_habit.user.pk,
                    "place": self.second_habit.place
                }
            ]
        })

    def test_list_public_habit(self):
        response = self.client.get(
            reverse('habits:habit_list_public')
        )

        self.assertEquals(response.status_code, status.HTTP_200_OK)

        self.assertEquals(response.json(), {
            "count": 2,
            "next": None,
            "previous": None,
            "results": [
                {
                    "id": self.first_habit.pk,
                    "bound_habit": self.first_habit.bound_habit,
                    "periodicity": self.first_habit.periodicity,
                    "duration": self.first_habit.duration,
                    "time": "11:00:00",
                    "action": self.first_habit.action,
                    "reward": self.first_habit.reward,
                    "is_pleasant": self.first_habit.is_pleasant,
                    "is_public": self.first_habit.is_public,
                    "user": self.first_habit.user.pk,
                    "place": self.first_habit.place
                },
                {
                    "id": self.second_habit.pk,
                    "bound_habit": self.second_habit.bound_habit,
                    "periodicity": self.second_habit.periodicity,
                    "duration": self.second_habit.duration,
                    "time": "13:00:00",
                    "action": self.second_habit.action,
                    "reward": self.second_habit.reward,
                    "is_pleasant": self.second_habit.is_pleasant,
                    "is_public": self.second_habit.is_public,
                    "user": self.second_habit.user.pk,
                    "place": self.second_habit.place
                }
            ]
        })

    def test_create_habit(self):
        response = self.client.post(
            reverse('habits:habit_create'),
            data={"time": "18:00", "action": "test", "duration": 45, "is_pleasant": False, "periodicity": 2,
                  "is_public": True, "reward": "test", "place": 'Home'}
        )

        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

        self.assertEquals(response.json(),
                          {'id': 3,
                           "bound_habit": None,
                           "periodicity": 2,
                           "duration": 45,
                           "time": "18:00:00",
                           "action": "test",
                           "reward": "test",
                           "is_pleasant": False,
                           "is_public": True,
                           "user": self.user.pk,
                           "place": 'Home'}
                          )

    def test_update_habit(self):
        response = self.client.patch(
            reverse('habits:habit_update', args=[self.first_habit.pk]),
            data={"time": "14:00"}
        )

        self.assertEquals(response.status_code, status.HTTP_200_OK)

        self.assertEquals(response.json(),
                          {"id": self.first_habit.pk,
                           "bound_habit": self.first_habit.bound_habit,
                           "periodicity": self.first_habit.periodicity,
                           "duration": self.first_habit.duration,
                           "time": "14:00:00",
                           "action": self.first_habit.action,
                           "reward": self.first_habit.reward,
                           "is_pleasant": self.first_habit.is_pleasant,
                           "is_public": self.first_habit.is_public,
                           "user": self.first_habit.user.pk,
                           "place": self.first_habit.place
                           }
                          )

    def test_delete_habit(self):
        response = self.client.delete(
            reverse('habits:habit_delete', args=[self.first_habit.pk])
        )
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
