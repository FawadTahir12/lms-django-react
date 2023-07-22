from django.urls import path
from . import views
urlpatterns = [
    path('teacher/',views.TeacherList.as_view()),
    path('teacher/<int:pk>', views.TeacherDetail.as_view()),
    path('teacher-login/', views.intructor_login),
    path('categories-list/', views.CategoryList.as_view()),
    path('course/', views.CourseList.as_view()),
    path('course-data/', views.CourseData.as_view()),
    path('instructor-change-password/<int:teacher_id>', views.intructor_change_password),

    path('course-chapters/<int:course_id>', views.ChaptersList.as_view()),
    path('instructor-courses/<int:instructor_id>', views.InstructorCourse.as_view()),
    path('chapter-data/<int:pk>', views.ChapterDetail.as_view()),
    path('course-detail/<int:pk>', views.CourseDetail.as_view()),
    path('teacher-detail/<int:pk>', views.TeacherDetailRetrieve.as_view()),
    # Student urls
    path('student/', views.StudentCreateList.as_view()),
    path('student-login/', views.student_login),
    path('student-enroll/', views.StudentEnrollList.as_view()),
    path('student-enroll-status/<int:course_id>/<int:student_id>', views.studentEnrollStatus),
    path('total-enroll-students-per-course/<int:course_id>/', views.StudentEnrollPerCourse.as_view()),
    path('course-rating/', views.CourseRating.as_view()),
    path('fetch-rating-status/<int:course_id>/<int:student_id>', views.studentRatingStatus),
    path('fetch-enrolled-students/<int:teacher_id>/', views.StudentEnrollPerCourse.as_view()),
    path('teacher/dashboard-data/<int:pk>', views.InstructorDashboardView.as_view()),
    path('fetch-enrolled-courses/<int:student_id>', views.StudentEnrollPerCourse.as_view()),
    path('fetch-recommended-courses/<int:student_id>', views.RecommendedCourses.as_view()),
    path('add-to-favorite-course/', views.FavoriteCoursesList.as_view()),
    path('fetch-favourite-status/<int:course_id>/<int:student_id>', views.CheckFavouriteCourseStatus),
    path('remove-favorite-course/<int:course_id>/<int:student_id>', views.removeFromFavoriteList),
    path('fetch-favorite-courses/<int:student_id>', views.FavoriteCoursesList.as_view()),
    path('student-assignment/<int:student_id>/<int:teacher_id>', views.StudentAssignmentList.as_view()),
    path('my-assignment/<int:student_id>', views.StudentAssignmentList.as_view()),
    path('update-assignment-status/<int:pk>', views.UpdateAssignment.as_view()),

]