from django import forms
from .models import Course, Submission, Department, Profile, Instructor, Student

# class EnrollmentForm(forms.Form):
#     course = forms.ChoiceField(choices=[(course.id, course.title) for course in Course.objects.all()])

class SubmissionForm(forms.ModelForm):
    class Meta:
        model = Submission
        fields = ['file', 'comments']

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['name']

class ProfileUpdateForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['profile_picture', 'bio']

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'department']

        
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

class InstructorForm(forms.ModelForm):
    class Meta:
        model = Instructor
        fields = '__all__'               