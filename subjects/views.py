from django.shortcuts import render, redirect, get_object_or_404
from subjects.models import Subject
from teachers.models import Teacher
from students.models import Student
from groups.models import Group


def home(request):
    ctx = {
        'subjects_count': Subject.objects.count(),
        'teachers_count': Teacher.objects.count(),
        'students_count': Student.objects.count(),
        'group_count': Group.objects.count(),
    }
    return render(request, 'index.html', ctx)

def subject_list(request):
    subjects = Subject.objects.all()
    ctx = {'subjects': subjects}
    return render(request, 'subjects/subjects-list.html', ctx)

def subject_add(request):
    if request.method == 'POST':
        subject_title = request.POST.get('subject_title')
        if subject_title:
            Subject.objects.create(
                subject_title=subject_title
            )
            return  redirect('subjects:list')
    return render(request, 'subjects/subject-form.html')


def subject_detail(request, subject_id):
    subject = get_object_or_404(Subject, pk=subject_id)
    ctx = {'subject': subject}
    return render(request, 'subjects/subject-detail.html', ctx)

def subject_delete(request, subject_id):
    subject = get_object_or_404(Subject, pk=subject_id)
    subject.delete()
    return redirect('subjects:list')

def subject_update(request, subject_id):
    subject = get_object_or_404(Subject, pk=subject_id)
    if request.method == 'POST':
        subject_title = request.POST.get('subject_title')
        if subject_title:
            subject.subject_title = subject_title
            subject.save()
            return redirect(subject.get_detail_url())
    ctx = {'subject': subject}
    return render(request, 'subjects/subject-form.html', ctx)