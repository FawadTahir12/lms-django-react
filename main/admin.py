from django.contrib import admin
from . import models

admin.site.register(models.Teacher)
admin.site.register(models.Student)
admin.site.register(models.CourseCategory)
admin.site.register(models.Course)
admin.site.register(models.CourseChapters)
admin.site.register(models.StudentCourseEnrollment)
admin.site.register(models.CourseRating)
admin.site.register(models.StudentAssignment)
admin.site.register(models.Notification)






