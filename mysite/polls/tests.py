from django.test import TestCase
import datetime
from django.utils import timezone
from .models import Question
# Create your tests here.


class QuestionModelTests(TestCase):

    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_quiz = Question(pub_date=time)
        self.assertIs(future_quiz.was_published_recently(), False)
    def test_was_published_recently_with_old_question(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is old.
        """
        time = timezone.now() - datetime.timedelta(days=5)
        old_question = Question(pub_date=time)
        self.assertIs(old_question.was_published_recently(), False)
    def test_was_published_recently_with_recent_question(self):
        """
        was_published_recently() returns True for questions whose pub_date
        is in the recent.
        """
        time = timezone.now() -  datetime.timedelta(hours=18 ,minutes=10)
        recent_question = Question(pub_date=time)
        self.assertIs(recent_question.was_published_recently(), True)