from django.db import models
from django.urls import reverse

from django.contrib.auth.models import User  # 8.2 引用django自身的User模型


# Create your models here.
class Course(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)   # 8.1.2给我们的User模型添加一个FK
    subject = models.CharField(default='', max_length=100)        # 8.1.2 保存course的subject是什么
    published = models.BooleanField(default=False)                # 8.2.5

    def __str__(self):
        return self.title


class Step(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    order = models.IntegerField(default=0)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    class Meta:
        abstract = True
        ordering = ['order', ]

    def __str__(self):
        return self.title


class Text(Step):
    content = models.TextField(blank=True, default='')

    def get_absolute_url(self):  # 2.3
        return reverse('courses:text_detail', kwargs={
            'course_pk': self.course_id,
            'step_pk': self.id})


class Quiz(Step):
    total_questions = models.IntegerField(default=4)
    times_taken = models.IntegerField(default=0, editable=False)   # 8.3.1， editable=False表示不会在admin中显示

    class Meta:
        verbose_name_plural = 'Quizzes'

    def get_absolute_url(self):  # 2.3
        return reverse('courses:quiz_detail', kwargs={
            'course_pk': self.course_id,
            'step_pk': self.id})


# 2.5
class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)  # quiz属性是外键,主键是Question的id/pk
    order = models.IntegerField(default=0)
    prompt = models.TextField()

    class Meta:
        ordering = ['order', ]

    def get_absolute_url(self):
        return self.quiz.get_absolute_url()

    def __str__(self):
        return self.prompt


class MultipleChoiceQuestion(Question):
    shuffle_answers = models.BooleanField(default=False)


class TrueFalseQuestion(Question):
    pass


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    order = models.IntegerField(default=0)
    text = models.CharField(max_length=255)
    correct = models.BooleanField(default=False)

    class Meta:
        ordering = ['order', ]

    def __str__(self):
        return self.text

