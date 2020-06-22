from django.contrib import admin
from .models import *


class QuestionAdmin(admin.ModelAdmin):
    list_filter = ('variant',)

class AnswerAdmin(admin.ModelAdmin):
    list_filter = ('student',)    


# Register your models here.
admin.site.register(Grade)
admin.site.register(Subject)
admin.site.register(Variant)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Student)
admin.site.register(Answer, AnswerAdmin)
admin.site.register(Teacher)
admin.site.register(Testing)
admin.site.register(Review)
