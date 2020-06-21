from django.contrib import admin
from .models import *


class QuestionAdmin(admin.ModelAdmin):
    list_filter = ('variant',)


# Register your models here.
admin.site.register(Grade)
admin.site.register(Subject)
admin.site.register(Variant)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Student)
admin.site.register(Answer)
admin.site.register(Teacher)
admin.site.register(Testing)
