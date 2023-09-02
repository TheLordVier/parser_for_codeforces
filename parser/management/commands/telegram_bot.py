import random

from django.conf import settings

from parser.models import Problem
import telebot

from django.core.management import BaseCommand

from parser.services import make_used_problem


class Command(BaseCommand):

    def handle(self, *args, **options) -> None:
        bot_token = settings.TELEGRAM_BOT_TOKEN

        bot = telebot.TeleBot(bot_token)

        @bot.message_handler(content_types=['text'])
        def start(message) -> None:
            if message.text == '/start':
                bot.send_message(message.from_user.id, "Choose difficulty from 0 to 3500")
                bot.register_next_step_handler(message, get_difficulty)

        def get_difficulty(message) -> None:
            global difficulty_choice
            difficulty_choice = message.text
            bot.send_message(message.from_user.id, 'Choose theme')
            bot.register_next_step_handler(message, get_topic)

        def get_topic(message) -> None:
            global topic_choice
            topic_choice = message.text
            bot.register_next_step_handler(message, get_result)

        def get_result(message) -> None:
            problems = Problem.objects.filter(rating=difficulty_choice, themes__in=topic_choice, is_used=False)
            problem_set = random.sample(problems, 10)
            make_used_problem(problem_set)
            bot.send_message(message.from_user.id, f'Your set: {problem_set}.')

        bot.polling(none_stop=True, interval=0)
