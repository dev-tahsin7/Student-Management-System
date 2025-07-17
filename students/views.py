from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from django.shortcuts import redirect
from .models import Student
from .forms import StudentForm

class StudentListView(ListView):
    model = Student
    template_name = 'students/student_list.html'
    context_object_name = 'students'

class StudentDetailView(DetailView):
    model = Student
    template_name = 'students/student_detail.html'
    context_object_name = 'student'

class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'students/student_form.html'
    success_url = reverse_lazy('student_list')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Student added successfully!')
        return response

class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'students/student_form.html'
    success_url = reverse_lazy('student_list')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Student updated successfully!')
        return response

class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'students/student_confirm_delete.html'
    success_url = reverse_lazy('student_list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Student deleted successfully!')
        return super().delete(request, *args, **kwargs)
