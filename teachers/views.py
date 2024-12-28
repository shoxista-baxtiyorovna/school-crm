from django.shortcuts import render, redirect, get_object_or_404
from teachers.models import Teacher


def teacher_list(request):
    teachers = Teacher.objects.all()
    ctx = {'teachers': teachers}
    return render(request, 'teachers/teachers-list.html', ctx)

def teacher_add(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        subject = request.POST.get('subject')
        phone_num = request.POST.get('phone_num')
        email = request.POST.get('email')
        experience = request.POST.get('experience')
        image = request.FILES.get('image')
        if first_name and last_name and subject and phone_num and email and experience and image:
            Teacher.objects.create(
                first_name=first_name,
                last_name=last_name,
                subject=subject,
                phone_num=phone_num,
                email=email,
                experience=experience,
                image=image
            )
            return  redirect('teachers:list')
    return render(request, 'teachers/teacher-form.html')


def teacher_detail(request, teacher_id):
    teacher = get_object_or_404(Teacher, pk=teacher_id)
    ctx = {'teacher': teacher}
    return render(request, 'subjects/subject-detail.html', ctx)

def teacher_delete(request, teacher_id):
    teacher = get_object_or_404(Teacher, pk=teacher_id)
    teacher.delete()
    return redirect('teachers:list')

def teacher_update(request, teacher_id):
    teacher = get_object_or_404(Teacher, pk=teacher_id)
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        subject = request.POST.get('subject')
        phone_num = request.POST.get('phone_num')
        email = request.POST.get('email')
        experience = request.POST.get('experience')
        image = request.FILES.get('image')
        if first_name and last_name and subject and phone_num and email and experience and image:
                teacher.first_name = first_name
                teacher.last_name = last_name
                teacher.subject = subject
                teacher.phone_num = phone_num
                teacher.email = email
                teacher.experience = experience
                teacher.image = image
                teacher.save()
                return redirect(teacher.get_detail_url())
    ctx = {'teacher': teacher}
    return render(request, 'subjects/subject-form.html', ctx)