import datetime

from polls.models import Choice, Question


def poll_question():
    question = Question.objects.create(
        question_text='What is your favorite color?',
        pub_date=datetime.datetime.now(),
    )
    Choice.objects.create(
        question=question,
        choice_text='Red',
    )
    Choice.objects.create(
        question=question,
        choice_text='Blue',
    )
    return question, (), {'pk': question.pk}
