
from django.shortcuts import render, redirect, get_object_or_404
from .models import Course, Student, Enrollment, Assignment, Submission,Instructor, Department,Announcement,Profile
from .forms import DepartmentForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from .forms import ProfileUpdateForm,CourseForm  
from .forms import InstructorForm
from django.shortcuts import render, get_object_or_404, redirect
from .models import Instructor
from .forms import InstructorForm

def create_instructor(request):
    if request.method == 'POST':
        form = InstructorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('instructor_list')  # Redirect to the list view
    else:
        form = InstructorForm()
    return render(request, 'create_instructor.html', {'form': form})

# def instructor_list(request):
#     instructors = Instructor.objects.all()
    
#     return render(request, 'instructor_list.html', {'instructors': instructors})
from django.http import JsonResponse
def instructor_list(request):
    instructors = Instructor.objects.all()
    instructor_data = [
        {
            'id': instructor.id,
            'name': instructor.name,
            'gender': instructor.gender,
            'date_of_birth': instructor.date_of_birth.strftime('%Y-%m-%d'),
            'department': instructor.department,
            'email': instructor.email,
            'contact_number': instructor.contact_number
        }
        for instructor in instructors
    ]
    
    response_data = {
        'status': 'success',
        'instructors': instructor_data
    }
    
    return JsonResponse(response_data, status=200)

def update_instructor_profile(request, instructor_id):
    instructor = get_object_or_404(Instructor, pk=instructor_id)
    if request.method == 'POST':
        form = InstructorForm(request.POST, instance=instructor)
        if form.is_valid():
            form.save()
            return redirect('instructor_list')
    else:
        form = InstructorForm(instance=instructor)
    return render(request, 'update_instructor_profile.html', {'form': form, 'instructor': instructor})

def delete_instructor_profile(request, instructor_id):
    instructor = get_object_or_404(Instructor, pk=instructor_id)
    if request.method == 'POST':
        instructor.delete()
        return redirect('instructor_list')
    return render(request, 'delete_instructor_profile.html', {'instructor': instructor})




def instructor_detail(request, instructor_id):
    instructor = get_object_or_404(Instructor, id=instructor_id)
    return render(request, 'instructor_detail.html', {'instructor': instructor})

def update_instructor(request, instructor_id):
    instructor = get_object_or_404(Instructor, id=instructor_id)
    if request.method == 'POST':
        form = InstructorForm(request.POST, instance=instructor)
        if form.is_valid():
            form.save()
            return redirect('instructor_list')
    else:
        form = InstructorForm(instance=instructor)
    return render(request, 'update_instructor.html', {'form': form, 'instructor': instructor})

def delete_instructor(request, instructor_id):
    instructor = get_object_or_404(Instructor, id=instructor_id)
    if request.method == 'POST':
        instructor.delete()
        return redirect('instructor_list')
    return render(request, 'delete_instructor.html', {'instructor': instructor})




@login_required
def edit_course(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    if request.method == 'POST':
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect('course_list')
    else:
        form = CourseForm(instance=course)
    return render(request, 'edit_course.html', {'form': form, 'course': course})

@login_required
def delete_course(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    if request.method == 'POST':
        course.delete()
        return redirect('course_list')
    return render(request, 'delete_course.html', {'course': course})

def course_list(request):
    courses = Course.objects.all()
    return render(request, 'course_list.html', {'courses': courses})



@login_required
def student_dashboard(request):
    # Fetch relevant data for student dashboard
    user_profile = Profile.objects.get(user=request.user)
    enrolled_courses = user_profile.enrolled_courses.all()

    context = {
        'enrolled_courses': enrolled_courses,
        'user_profile': user_profile,
    }

    return render(request, 'student_dashboard.html', context)

@login_required
def instructor_dashboard(request):
    # Fetch relevant data for instructor dashboard
    user_profile = Profile.objects.get(user=request.user)
    taught_courses = user_profile.taught_courses.all()

    context = {
        'taught_courses': taught_courses,
        'user_profile': user_profile,
    }

    return render(request, 'instructor_dashboard.html', context)

@login_required
def student_dashboard(request):
    return render(request, 'student_dashboard.html')

@login_required
def instructor_dashboard(request):
    return render(request, 'instructor_dashboard.html')
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')  # Redirect to the user's dashboard
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')  # Redirect to the user's dashboard
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('login')  # Redirect to the login page

def course_list(request):
    courses = Course.objects.all()
    return render(request, 'course_list.html', {'courses': courses})


def enroll_course(request):
    if request.method == 'POST':
        student = request.user.student  # Assuming you have a Student model and authenticated user
        course_id = request.POST.get('course_id')
        course = Course.objects.get(id=course_id)
        enrollment = Enrollment(student=student, course=course)
        enrollment.save()
        return redirect('course_list')  # Redirect to course list or any other appropriate page

    # Redirect to the course list if accessed via GET
    return redirect('course_list')


def assignment_details(request, assignment_id):
    assignment = get_object_or_404(Assignment, id=assignment_id)
    context = {'assignment': assignment}
    return render(request, 'myapp/assignment_details.html', context)


def submit_assignment(request, assignment_id):
    if request.method == 'POST':
        student = request.user.student  # Assuming you have a Student model and authenticated user
        assignment = Assignment.objects.get(id=assignment_id)
        submission = Submission(student=student, assignment=assignment)
        submission.file = request.FILES['file']  # Assuming file input name is 'file'
        submission.comments = request.POST.get('comments')
        submission.save()
        return redirect('course_list')  # Redirect to course list or any other appropriate page

    assignment = Assignment.objects.get(id=assignment_id)
    context = {'assignment': assignment}
    return render(request, 'myapp/submit_assignment.html', context)

def department_management(request):
    departments = Department.objects.all()
    context = {'departments': departments}
    return render(request, 'department_management.html', context)

def edit_department(request, department_id):
    department = get_object_or_404(Department, id=department_id)

    if request.method == 'POST':
        department.name = request.POST['department_name']
        department.save()
        return redirect('department_management')

    context = {'department': department}
    return render(request, 'department_edit.html', context)

def delete_department(request, department_id):
    department = get_object_or_404(Department, id=department_id)

    if request.method == 'POST':
        department.delete()
        return redirect('department_management')

    context = {'department': department}
    return render(request, 'department_delete.html', context)

def announcement_management(request):
    announcements = Announcement.objects.all()
    return render(request, 'announcement_management.html', {'announcements': announcements})

def add_announcement(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        announcement = Announcement(title=title, content=content)
        announcement.save()
        return redirect('announcement_management')

    return render(request, 'announcement_add.html')

def edit_announcement(request, announcement_id):
    announcement = get_object_or_404(Announcement, id=announcement_id)

    if request.method == 'POST':
        announcement.title = request.POST['title']
        announcement.content = request.POST['content']
        announcement.save()
        return redirect('announcement_management')

    context = {'announcement': announcement}
    return render(request, 'announcement_edit.html', context)

def delete_announcement(request, announcement_id):
    announcement = get_object_or_404(Announcement, id=announcement_id)

    if request.method == 'POST':
        announcement.delete()
        return redirect('announcement_management')

    context = {'announcement': announcement}
    return render(request, 'announcement_delete.html', context)

def add_department(request):
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('department_management')  # Redirect to department management page
    else:
        form = DepartmentForm()
    context = {'form': form}
    return render(request, 'add_department.html', context)



    department = get_object_or_404(Department, id=department_id)

    if request.method == 'POST':
        form = DepartmentForm(request.POST, instance=department)
        if form.is_valid():
            form.save()
            return redirect('department_management')
    else:
        form = DepartmentForm(instance=department)

    context = {'form': form, 'action': 'Edit'}
    return render(request, 'edit_department.html', context)

@login_required
def profile_update(request):
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Redirect to the user's profile view
    else:
        form = ProfileUpdateForm(instance=request.user.profile)
    
    context = {'form': form}
    return render(request, 'profile_update.html', context)
