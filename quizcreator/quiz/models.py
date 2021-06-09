from django.db import models


# Create your models here.


class Quiz(models.Model):
    quiz_name = models.CharField(max_length=100, null=False, blank=False)
    description = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        app_label = 'quiz'


class Question(models.Model):
    question = models.CharField(max_length=255, null=False, blank=False)

    class Meta:
        app_label = 'quiz'


class QuizSession(models.Model):
    quiz_of = models.ForeignKey(to=Quiz, on_delete=models.CASCADE)
    questions = models.ManyToManyField(Question)

    class Meta:
        app_label = 'quiz'


class Choices(models.Model):
    choice_value = models.CharField(max_length=25, null=False, blank=False)
    question_related_to = models.ForeignKey(to=Question, on_delete=models.CASCADE)

    class Meta:
        app_label = 'quiz'


class Answer(models.Model):
    answer_value = models.ForeignKey(to=Choices, on_delete=models.CASCADE)
    question_related_to = models.ForeignKey(to=Question, on_delete=models.CASCADE)

    class Meta:
        app_label = 'quiz'

class Student(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    enroll_number = models.CharField(max_length=20, null=False, blank=False, unique=True)

    class Meta:
        app_label = 'quiz'


class StudentQuizSession(models.Model):
    quiz_related = models.ForeignKey(to=Quiz, on_delete=models.CASCADE)
    question = models.ManyToManyField(QuizSession)
    student = models.ForeignKey(to=Student, on_delete=models.CASCADE)

    class Meta:
        app_label = 'quiz'