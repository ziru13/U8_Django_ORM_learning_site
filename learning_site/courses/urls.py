from django.urls import path
from . import views

app_name = 'courses'

# make our variable, a list, in the old Django, it didn't use to be a list, now it's just a list
urlpatterns = [
    path('', views.course_list, name='course_list'),
    path('<int:course_pk>/t<int:step_pk>/', views.text_detail, name='text_detail'),  # 2.3
    path('<int:course_pk>/q<int:step_pk>/', views.quiz_detail, name='quiz_detail'),  # 2.3
    # path('<int:course_pk>/<int:step_pk>/', views.step_detail, name='step_detail'), # 在2.3去掉
    path('<int:course_pk>/create_quiz/', views.quiz_create, name='quiz_create'),
    path('<int:course_pk>/edit_quiz/<int:quiz_pk>/', views.quiz_edit, name='quiz_edit'),
    path('<int:quiz_pk>/create_question/<question_type>/', views.create_question, name='create_question'),
    path('<int:quiz_pk>/edit_question/<int:question_pk>/', views.edit_question, name='edit_question'),
    path('<int:question_pk>/create_answer/', views.answer_form, name='create_answer'),
    path('<int:pk>/', views.course_detail, name='course_detail'),
    path('by/<teacher>', views.courses_by_teacher, name='courses_by_teacher'),  # 8.2.1
    path('search/', views.search, name='search'),   # 8.2.3
]