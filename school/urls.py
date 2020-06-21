from django.urls import path
from . import views
# from .views import *
from django.urls import reverse_lazy

urlpatterns = [
    path('',                views.index,            name='index'),
    path('rate',            views.rate,             name='rate'),
    # path('',                views.check,            name = 'check'),
    path('input',           views.input,            name='input'),
    path('test',            views.test,             name='test'),
    path('pag',             views.pagination,       name='pag'),
    path('new',             views.new,       name='new'),
    path('pagination_p/<student>/<grade>/<variant_of_subject>',
         views.pagination_pro,   name='pagination_p'),
    path('serial_answers',  views.serial_answers,   name='serial_answers'),
    path('create_test',     views.create_test,      name='create_test'),
    path('moderator',       views.moderator,         name='moderator'),
    path('testing_page/<grade>/<student>',
         views.testing_page,     name='testing_page'),
    path('deadline',    views.deadline,     name="deadline"),
    path('sign_in', views.sign_in, name='sign_in'),
    path('sign_in_test', views.sign_in_test, name='sign_in_test'),
    path('create_user',     views.create_user,      name='create_user'),
]
