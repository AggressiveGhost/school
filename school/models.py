from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.utils.timezone import now
from datetime import timedelta
# import timedelta


class Grade(models.Model):
    grade = models.PositiveIntegerField()
    duration = models.DurationField(blank=True, default=timedelta())

    def __str__(self):
        return str(self.grade)


class Subject(models.Model):
    subject = models.CharField('Subject', max_length=100,)
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE)

    def __str__(self):
        return '{0} {1}'.format(self.subject, self.grade.grade)
        # return self.subject


class Variant(models.Model):
    variant = models.PositiveIntegerField()
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)

    def get_absolute_url(self):
        return reverse('pagination_p', kwargs={'variant_of_subject': self.id})


class Teacher(models.Model):
    teacher = models.ManyToManyField(User)

    def __str__(self):
        return 'teacher'




class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    school = models.CharField('school', max_length=40, blank=True)
    phone = models.CharField('phone', max_length=20, blank=True, unique=True)
    parents_phone = models.CharField(
        'parents_phone', max_length=20, blank=True)
    result = models.CharField('result', max_length=4, blank=True)
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE)
    address = models.TextField(blank=True)
    start = models.DateTimeField(default=now)

    def __str__(self):
        return self.user.first_name + " " + str(self.id)

class Review(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    grade = models.PositiveIntegerField()
    status = models.BooleanField(default=False)
    

    def __str__(self):
        return 'review'


class Question(models.Model):
    question = models.ImageField(upload_to='questions', blank=True)
    variant = models.ForeignKey(Variant, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)


class Answer(models.Model):
    answer = models.TextField(blank=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    def __str__(self):
        return self.answer


class Testing(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    variant = models.ForeignKey(Variant, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)


class AnswerCheck(models.Model):
    page = models.PositiveIntegerField()
    id_answer = models.PositiveIntegerField()
    answer = models.BooleanField(default=False)
