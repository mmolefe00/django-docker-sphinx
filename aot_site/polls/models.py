# === IMPORTS === #
from django.db import models

# -------------
# POLLS MODELS
# -------------

# === QUESTION MODEL === #
class Question(models.Model):
    """This class models a specific poll question field with an accompanying date
    and returns the question text. Choices for each question are subsequently created in
    the :class:`Choice` model.

    :param question_text: Field with displayed text for each question
    :type question_text: models.CharField(max_length=200)
    :param date_published: Field for the date the question is published
    :type date_published: models.DateTimeField('date_published')
    """

    # displays the question as well as the published date
    question_text = models.CharField(max_length=200)  # our primary key
    date_published = models.DateTimeField('date_published')

    # to string to return question
    def __str__(self):
        """Return a string representation of the question."""
        return self.question_text


# === CHOICE MODEL === #
class Choice(models.Model):
    """This class model creates choice options under a specific question and allows users to vote
    on said choice options. The specific question stems from the :class:`~Question` model.

     :param question: The question the choices belong to. Should be a :class:`~Question` instance.
     :type question: Question
     :param choice_text: Field with displayed text for a single choice option.
     :type choice_text: str
     :param votes: Counts the number of votes for a single choice option.
     :type votes: int
     """

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)


    def __str__(self):
        """Return a string representation of the choice option."""
        return self.choice_text


# === END === #
