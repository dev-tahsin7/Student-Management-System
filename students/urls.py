from django.urls import path
from . import views

urlpatterns = [
    path('', views.StudentListView.as_view(), name='student_list'),
    path('student/<int:pk>/', views.StudentDetailView.as_view(), name='student_detail'),
    path('student/add/', views.StudentCreateView.as_view(), name='student_add'),
    path('student/<int:pk>/edit/', views.StudentUpdateView.as_view(), name='student_edit'),
    path('student/<int:pk>/delete/', views.StudentDeleteView.as_view(), name='student_delete'),
] 