from django.shortcuts import render, redirect, get_object_or_404
from . import models, forms
from django.core.paginator import Paginator
from django.views import generic
#CRUD - CREATE READ UPDATE DELETE

#create

class CreateStudent(generic.CreateView):
    model = models.Student
    form_class = forms.StudentForm
    template_name = 'students/create_student.html'
    success_url = '/student_list/'


# def createStudent(request):
#     if request.method == 'POST':
#         form = forms.StudentForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('student_list')
#     else:
#         form = forms.StudentForm()
#     return render(request, template_name='students/create_student.html',
#                   context={'form': form})

#read

class ReadStudent(generic.ListView):
    model = models.Student
    template_name = 'students/student_list.html'
    context_object_name = 'stud'
    paginate_by = 2

# def readStudent(request):
#     if request.method == 'GET':
#         student = models.Student.objects.all().order_by('-id')
#         paginator = Paginator(student, 2)
#         page = request.GET.get("page")
#         page_obj = paginator.get_page(page)
#     return render(request, template_name='students/student_list.html', 
#                   context={'stud': page_obj})

        
#update
class UpdateStudent(generic.UpdateView):
    model = models.Student
    form_class = forms.StudentForm
    template_name = 'students/update_student.html'
    success_url = '/student_list/'


    def get_object(self, *args, **kwargs):
        student_id = self.kwargs.get('id')
        return get_object_or_404(models.Student, id=student_id)
    
    def form_valid(self, form):
        print(form.cleaned_data)
        return super(UpdateStudent, self).form_valid(form=form)



# def updateStudent(request, id):
#     student_id = get_object_or_404(models.Student, id=id)
#     if request.method == 'POST':
#          form = forms.StudentForm(request.POST, instance=student_id)
#          if form.is_valid():
#              form.save()
#              return redirect('student_list')
#     else:
#         form = forms.StudentForm(instance=student_id)
    
#     return render(request, template_name='students/update_student.html',
#                   context={
#                       'form': form,
#                       "student_id": student_id,
#                       })


#delete

class DeleteStudent(generic.DeleteView):
    template_name = 'students/confirm_delete.html'
    success_url = '/student_list/'
    
    def get_object(self, *args, **kwags):
        student_id = self.kwargs.get('id')
        return get_object_or_404(models.Student, id=student_id)

# def deleteStudent(request, id):
#     student_id = get_object_or_404(models.Student, id=id)
#     student_id.delete()
#     return redirect('student_list')