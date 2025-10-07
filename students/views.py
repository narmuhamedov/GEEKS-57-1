from django.shortcuts import render, redirect, get_object_or_404
from . import models, forms


#CRUD - CREATE READ UPDATE DELETE

#create
def createStudent(request):
    if request.method == 'POST':
        form = forms.StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = forms.StudentForm()
    return render(request, template_name='students/create_student.html',
                  context={'form': form})

#read
def readStudent(request):
    if request.method == 'GET':
        student = models.Student.objects.all().order_by('-id')
    return render(request, template_name='students/student_list.html', 
                  context={'stud': student})

        
#update
def updateStudent(request, id):
    student_id = get_object_or_404(models.Student, id=id)
    if request.method == 'POST':
         form = forms.StudentForm(request.POST, instance=student_id)
         if form.is_valid():
             form.save()
             return redirect('student_list')
    else:
        form = forms.StudentForm(instance=student_id)
    
    return render(request, template_name='students/update_student.html',
                  context={
                      'form': form,
                      "student_id": student_id,
                      })


#delete
def deleteStudent(request, id):
    student_id = get_object_or_404(models.Student, id=id)
    student_id.delete()
    return redirect('student_list')