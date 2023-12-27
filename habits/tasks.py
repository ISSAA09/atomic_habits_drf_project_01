import os
from celery import shared_task
from habits.models import Habit
import requests
from datetime import datetime, time


@shared_task()
def habit_bot():
    now = datetime.utcnow()
    time_ = time(now.time().hour, now.time().minute, 0)
    send_habit = Habit.objects.filter(time=time_)
    for h in send_habit:
        action = h.action
        time_h = h.time
        place = h.place

        text = f'Я должен {action} в {time_h} в {place}'
        params = {
            "chat_id": os.getenv('CHANNEL_ID'),
            'text': text
        }
        requests.get(f"https://api.telegram.org/bot"
                     f"{os.getenv('TELEGRAM_API_TOKEN')}/"
                     f"sendMessage", params=params)
