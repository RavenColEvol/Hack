from django.urls import path
from main import views

urlpatterns = [
    path('',views.IndexView.as_view(),name='index'),
    path('problem_list/',views.CompanyProblemsList.as_view(),name='problem_list'),
    path('student_form/',views.StudentFormView,name='student_form'),
    path('email/',views.test_email,name='email')
]