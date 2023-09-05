from django.urls import path
from . import views  # Import your app's views

urlpatterns = [
    # Other URL patterns
    path('courses/', views.course_list, name='course_list'),
    path('courses/create/', views.create_course, name='create_course'),
   
    path('enroll/', views.enroll_student, name='enroll_course'),
    # path('confirmation/', views.confirmation_page, name='confirmation_page'),
    path('confirmation/<int:student_id>/', views.confirmation_page, name='confirmation_page'),

   
    path('assignments/', views.assignment_list, name='assignment_list'),
    path('assignments/create/<int:course_id>/', views.create_assignment, name='create_assignment'),
   


    path('assignments/<int:assignment_id>/delete/', views.delete_assignment, name='delete_assignment'),
    path('assignments/<int:assignment_id>/', views.assignment_details, name='assignment_details'),
    path('assignments/<int:assignment_id>/submit/', views.submit_assignment, name='submit_assignment'),
 
    path('assignments/<int:assignment_id>/update/', views.update_assignment, name='update_assignment'),



    path('department-management/', views.department_management, name='department_management'),
    path('departments/edit/<int:department_id>/', views.edit_department, name='edit_department'),
    path('departments/delete/<int:department_id>/', views.delete_department, name='delete_department'),
    path('announcements/', views.announcement_management, name='announcement_management'),
    path('announcements/add/', views.add_announcement, name='add_announcement'),
    path('announcements/edit/<int:announcement_id>/', views.edit_announcement, name='edit_announcement'),
    path('announcements/delete/<int:announcement_id>/', views.delete_announcement, name='delete_announcement'),
    path('departments/add/', views.add_department, name='add_department'),
    path('dashboard/student/', views.student_dashboard, name='student_dashboard'),
   
    path('profile/update/', views.profile_update, name='profile_update'),
    path('student/dashboard/', views.student_dashboard, name='student_dashboard'),
    

    path('courses/<int:course_id>/edit/', views.edit_course, name='edit_course'),
    path('courses/<int:course_id>/delete/', views.delete_course, name='delete_course'),
    # path('courses/', views.course_list, name='course_list'),

    path('students/', views.student_list, name='student_list'),
    path('students/create/', views.create_student, name='create_student'),
    path('students/<int:student_id>/update/', views.update_student_profile, name='update_student_profile'),
    path('students/<int:student_id>/delete/', views.delete_student_profile, name='delete_student_profile'),



    path('instructor/dashboard/', views.instructor_dashboard, name='instructor_dashboard'),
    path('instructors/', views.instructor_list, name='instructor_list'),
    path('instructors/<int:instructor_id>/', views.instructor_detail, name='instructor_detail'),
    path('instructors/<int:instructor_id>/update/', views.update_instructor, name='update_instructor'),
    path('instructors/<int:instructor_id>/delete/', views.delete_instructor, name='delete_instructor'),
    path('instructors/create/', views.create_instructor, name='create_instructor'),

]