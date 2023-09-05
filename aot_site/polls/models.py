# === IMPORTS === #
from django.db import models

# -------------
# POLLS MODELS
# -------------

# === QUESTION MODEL === #
class Question(models.Model):
    """This class model creates a specific poll question field with an accompanying date
    and returns the question text. Choices for each question are subsequently created in
    the :class: 'Choice(models.Model)' class.

    :param models.CharField(max_length=200) question_text: Field with displayed text for each question
    :param models.DateTimeField('date_published') date_published: Field for the date the question is published
    """


    # displays the question as well as the published date
    question_text = models.CharField(max_length=200)  # our primary key
    date_published = models.DateTimeField('date_published')

    # to string to return question
    def __str__(self):
        """to string to return question text"""
        return self.question_text


# === CHOICE MODEL === #
class Choice(models.Model):
    """This class model creates choice options under a specific question and allows users to vote
    on said choice options. The specific question stems from :class: 'Question(models.Model)'

    :param models.ForeignKey() question: The question the choices belong to
    :param models.CharField(max_length=200) choice_text: Field with displayed text for a single choice option
    :param models.IntegerField(default=0)  votes: Counts the amount of votes for a single choice option
    """

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)


    def __str__(self):
        """to string to return choice text"""
        return self.choice_text


# === END === #
