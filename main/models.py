from django.db import models
from django.core import serializers
from django.db.models import Q


# Create your models here.

class Teacher(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    about = models.TextField(default=None)
    password = models.CharField(max_length=100, blank=True, null=True)
    qualification = models.CharField(max_length=200)
    mobile_no = models.CharField(max_length=20)
    skills = models.TextField()
    profile_photo = models.ImageField(upload_to='teacher-profile-imgs/', null=True)

    def total_teacher_courses(self):
        total_courses = Course.objects.filter(teacher=self).count()
        return total_courses

    def total_teacher_chapters(self):
        total_chapters = CourseChapters.objects.filter(course__teacher=self).count()
        return total_chapters

    def total_enrolled_students(self):
        total_enrolled_students = StudentCourseEnrollment.objects.filter(course__teacher=self).count()
        return total_enrolled_students

    def __str__(self):
        return self.full_name


class CourseCategory(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title


class Course(models.Model):
    category = models.ForeignKey(CourseCategory, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='teacher_course')
    title = models.CharField(max_length=200)
    description = models.TextField()
    course_image = models.ImageField(upload_to='course-imgs/', null=True)
    technologies = models.TextField(null=True)

    def related_courses(self):
        tech_list = self.technologies.split(',')
        query = Q()
        for skill in tech_list:
            query |= Q(technologies__icontains=skill)

        courses = Course.objects.filter(query).exclude(id=self.id)
        # courses = courses_all.exclude(id=self.id)
        return serializers.serialize('json', courses)

    def tech_list(self):
        tech_list = self.technologies.split(',')
        return tech_list

    def total_enrolled_student(self):
        total_enrolled = StudentCourseEnrollment.objects.filter(course=self).count()
        return total_enrolled

    def avg_course_rating(self):
        course_rating = CourseRating.objects.filter(course=self).aggregate(avg_rating=models.Avg('rating'))
        if course_rating['avg_rating'] is None:
            return 0
        return str(course_rating['avg_rating'])[:3]

    def __str__(self):
        return self.title


class CourseChapters(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='course_chapter')
    title = models.CharField(max_length=200)
    description = models.TextField()
    video = models.FileField(upload_to='course-videos', null=True)
    remarks = models.TextField(null=True)

    def __str__(self):
        return self.title


class Student(models.Model):
    full_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    mobile_no = models.CharField(max_length=20)
    interests = models.TextField()

    def __str__(self):
        return self.full_name


class StudentCourseEnrollment(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='enrolled_courses')
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='enrolled_student')
    enrolled_time = models.DateTimeField(auto_now_add=True)


class CourseRating(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='course_rating')
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='student_rating')
    rating = models.PositiveBigIntegerField(default=0)
    reviews = models.TextField(null=True)
    review_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.course}-{self.student}-{self.rating}"


class FavoriteCourses(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='favorite_course')
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='student_favorite')
    status = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.course}-{self.student}-favorite"


class StudentAssignment(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='teacher_assignment')
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='student_assignment')
    title = models.CharField(max_length=200)
    detail = models.TextField(null=True)
    add_time = models.DateTimeField(auto_now_add=True)
    student_assignment_status = models.BooleanField(default=False, null=True)

    def __str__(self):
        return self.title
