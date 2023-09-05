from django import forms
from .models import Course, Submission, Department, Profile, Instructor, Student, Enrollment

class EnrollmentForm(forms.ModelForm):
    class Meta:
        model = Enrollment
        fields = ['student', 'course', 'enrollment_date']

    widgets = {
        'enrollment_date': forms.DateInput(attrs={'type': 'date'}),
    }

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