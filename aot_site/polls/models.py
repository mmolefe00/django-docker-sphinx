# === IMPORTS === #
from django.db import models

# -------------
# POLLS MODELS
# -------------

# === QUESTION MODEL === #
class Question(models.Model):

    # displays the question as well as the published date
    question_text = models.CharField(max_length=200)  # our primary key
    date_published = models.DateTimeField('date_published')

    # to string to return question
    def __str__(self):

        return self.question_text


# === CHOICE MODEL === #
class Choice(models.Model):

    # foreign key from Question class
    # on_delete=models.CASCADE means that when we delete the poll question, all the choice options delete with it.
    question = models.ForeignKey(Question, on_delete=models.CASCADE)


    # field for each choice under the question
    choice_text = models.CharField(max_length=200)


    # counts all our votes for each choice (under the main question)
    # if we delete the choice with on_delete, the votes will be auto-deleted.
    votes = models.IntegerField(default=0)

    # to string to return choice text
    def __str__(self):

        return self.choice_text


# === END === #
