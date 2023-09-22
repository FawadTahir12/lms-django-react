from rest_framework import serializers
from . import models


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Teacher
        fields = ['id', 'full_name', 'email', 'password', 'qualification', 'mobile_no', 'skills', 'profile_photo',
                  'about']
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data.pop('password', None)  # Exclude 'password' field from representation
        return data


class InstructorDashboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Teacher
        fields = ['total_teacher_chapters', 'total_teacher_courses', 'total_enrolled_students']


class StudentDashboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Student
        fields = ['total_enrolled_courses', 'total_favorite_courses', 'complete_assignments', 'pending_assignments']


class CourseCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CourseCategory
        fields = ['id', 'title', 'description']


class AllCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Course
        fields = ['id', 'category', 'teacher', 'title', 'description', 'course_image', 'technologies', 'course_chapter',
                  'related_courses', 'tech_list', 'total_enrolled_student', 'avg_course_rating']
        depth = 1

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["teacher"].pop('password', None)  # Exclude 'password' field from representation
        data["teacher"].pop('mobile_no', None)  # Exclude 'mobile_no' field from representation
        # Exclude 'password' field from representation
        return data


class CourseChapterSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CourseChapters
        fields = ['id', 'course', 'title', 'description', 'video', 'remarks']


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Course
        fields = ['id', 'category', 'teacher', 'title', 'description', 'course_image', 'technologies',
                  'total_enrolled_student', 'avg_course_rating']


class TeacherDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Teacher
        fields = ['id', 'full_name', 'email', 'qualification', 'skills', 'about', 'teacher_course', 'profile_photo']
        depth = 1

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data.pop('password', None)  # Exclude 'password' field from representation
        return data


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Student
        fields = ['id', 'full_name', 'email', 'password', 'interests', 'mobile_no', 'username']
        extra_kwargs = {
            'password': {'write_only': True},
            'mobile_no': {'write_only': True}
        }

    def validate_email(self, value):
        if models.Student.objects.filter(email=value).exists() or models.Teacher.objects.filter(email=value).exists():
            raise serializers.ValidationError("User with this email already exists.")
        return value

    def validate_username(self, value):
        if models.Student.objects.filter(username=value).exists():
            raise serializers.ValidationError("Username Already taken")
        return value


class StudentDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Student
        fields = ['id', 'full_name', 'email', 'interests', 'mobile_no', 'username', 'profile_photo']


class StudentEnrollSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.StudentCourseEnrollment
        fields = ['course', 'student', 'enrolled_time']


class StudentEnrollPerCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.StudentCourseEnrollment
        fields = ['id', 'course', 'student', 'enrolled_time']
        depth = 2

    def to_representation(self, instance):
        data = super().to_representation(instance)

        data["student"].pop('password', None)  # Exclude 'password' field from representation
        data["student"].pop('mobile_no', None)  # Exclude 'mobile_no' field from representation
        data["course"]["teacher"].pop('password', None)  # Exclude 'mobile_no' field from representation

        # Exclude 'password' field from representation
        return data


class CourseRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CourseRating
        fields = ['id', 'course', 'student', 'rating', 'reviews', 'review_time']

    def __init__(self, *args, **kwargs):
        super(CourseRatingSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        self.Meta.depth = 0
        if request and request.method == 'GET':
            self.Meta.depth = 1


class FavoriteCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.FavoriteCourses
        fields = ['id', 'course', 'student']

    def __init__(self, *args, **kwargs):
        super(FavoriteCourseSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        self.Meta.depth = 0
        if request and request.method == 'GET':
            self.Meta.depth = 2


class StudentAssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.StudentAssignment
        fields = ['id', 'student', 'teacher', 'title', 'detail', 'add_time', 'student_assignment_status']

    def __init__(self, *args, **kwargs):
        super(StudentAssignmentSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        self.Meta.depth = 0
        if request and request.method == 'GET':
            self.Meta.depth = 1
        if request and request.method == 'GET' and 'pk' in request.parser_context['kwargs']:
            self.Meta.depth = 0

    def to_representation(self, instance):
        data = super().to_representation(instance)
        request = self.context.get('request')
        if 'pk' in request.parser_context['kwargs']:
            return data

        # data["teacher"].pop('password', None)  # Exclude 'password' field from representation
        # data["student"].pop('password', None)  # Exclude 'password' field from representation
        # data["student"].pop('mobile_no', None)  # Exclude 'password' field from representation
        # data["teacher"].pop('mobile_no', None)  # Exclude 'mobile_no' field from representation
        # data["teacher"].pop('qualification', None)  # Exclude 'mobile_no' field from representation
        # data["teacher"].pop('about', None)  # Exclude 'mobile_no' field from representation
        # data["teacher"].pop('profile_photo', None)  # Exclude 'mobile_no' field from representation

        # Exclude 'password' field from representation
        return data


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Notification
        fields = ['id', 'student', 'teacher', 'notif_subject', 'notif_for', 'notif_read_status', 'notif_created_time']
