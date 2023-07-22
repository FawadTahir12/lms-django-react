from django.shortcuts import render
from .serializers import TeacherSerializer, CourseCategorySerializer, CourseSerializer, CourseChapterSerializer, \
    AllCourseSerializer, TeacherDetailSerializer, StudentSerializer, StudentEnrollSerializer, \
    StudentEnrollPerCourseSerializer, CourseRatingSerializer, InstructorDashboardSerializer, \
    FavoriteCourseSerializer, StudentAssignmentSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import JsonResponse, HttpResponse
from rest_framework import generics
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import csrf_exempt
from . import models
from django.db.models import Q

from rest_framework.permissions import IsAuthenticated


# Create your views here.
def index(request):
    return HttpResponse("Hello World")
class TeacherList(generics.ListCreateAPIView):
    # def get(self, request):
    #     queryset = models.Teacher.objects.all()
    #     serializer = TeacherSerializer(queryset, many=True)
    #     return Response(serializer.data)
    queryset = models.Teacher.objects.all()
    serializer_class = TeacherSerializer

    # permission_classes = [IsAuthenticated]

    def list(self, request, **kwargs):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        serializer = TeacherSerializer(queryset, many=True)
        return Response(serializer.data)


class TeacherDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Teacher.objects.all()
    serializer_class = TeacherSerializer
    # permission_classes = [IsAuthenticated]


class TeacherDetailRetrieve(generics.RetrieveAPIView):
    queryset = models.Teacher.objects.all()
    serializer_class = TeacherDetailSerializer


@csrf_exempt
def intructor_login(request):
    email = request.POST['email']
    password = request.POST['password']
    try:
        instructorExist = models.Teacher.objects.get(email=email, password=password)
        if instructorExist:
            print(instructorExist.id, "id")
            return JsonResponse({
                'bool': True,
                'full_name': instructorExist.full_name,
                'id': instructorExist.id,
                'email': instructorExist.email
            })
    except ObjectDoesNotExist:
        return JsonResponse({
            'bool': False
        })


class CategoryList(generics.ListCreateAPIView):
    # def get(self, request):
    #     queryset = models.Teacher.objects.all()
    #     serializer = TeacherSerializer(queryset, many=True)
    #     return Response(serializer.data)
    queryset = models.CourseCategory.objects.all()
    serializer_class = CourseCategorySerializer

    # permission_classes = [IsAuthenticated]

    def list(self, request, **kwargs):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        serializer = CourseCategorySerializer(queryset, many=True)
        return Response(serializer.data)


class CourseList(generics.ListCreateAPIView):
    # def get(self, request):
    #     queryset = models.Teacher.objects.all()
    #     serializer = TeacherSerializer(queryset, many=True)
    #     return Response(serializer.data)
    queryset = models.Course.objects.all()
    serializer_class = CourseSerializer

    # permission_classes = [IsAuthenticated]
    def get_queryset(self):
        queryset = super().get_queryset()
        if 'result' in self.request.GET:
            limit = int(self.request.GET['result'])
            queryset = models.Course.objects.all().order_by('-id')[:limit]
        if 'category' in self.request.GET:
            category = self.request.GET['category']
            queryset = models.Course.objects.filter(technologies__icontains=category)
        if 'student_id' in self.kwargs:
            student_id = self.kwargs['student_id']
            student = models.Student.objects.get(pk=student_id)
            interests = student.interests.split(',')
            query = Q()
            for interest in interests:
                query |= Q(technologies__icontains=interest)
            queryset = models.Course.objects.filter(query)

        return queryset

    def list(self, request, **kwargs):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        serializer = CourseSerializer(queryset, many=True)
        return Response(serializer.data)


class InstructorCourse(generics.ListAPIView):
    serializer_class = CourseSerializer

    def get_queryset(self):
        instructor_id = self.kwargs['instructor_id']
        data = models.Course.objects.filter(teacher_id=instructor_id)
        return data


class ChaptersList(generics.ListCreateAPIView):
    # def get(self, request):
    #     queryset = models.Teacher.objects.all()
    #     serializer = TeacherSerializer(queryset, many=True)
    #     return Response(serializer.data)
    serializer_class = CourseChapterSerializer

    # permission_classes = [IsAuthenticated]
    def get_queryset(self):
        course_id = self.kwargs['course_id']
        course = models.Course.objects.get(pk=course_id)
        data = models.CourseChapters.objects.filter(course=course_id)
        return data

    def list(self, request, **kwargs):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        serializer = CourseChapterSerializer(queryset, many=True)
        return Response(serializer.data)


class ChapterDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.CourseChapters.objects.all()
    serializer_class = CourseChapterSerializer


class CourseDetail(generics.RetrieveUpdateDestroyAPIView):
    # def get(self, request):
    #     queryset = models.Teacher.objects.all()
    #     serializer = TeacherSerializer(queryset, many=True)
    #     return Response(serializer.data)
    queryset = models.Course.objects.all()
    serializer_class = AllCourseSerializer


class CourseData(generics.ListCreateAPIView):
    queryset = models.Course.objects.all()
    serializer_class = CourseSerializer


class StudentCreateList(generics.ListCreateAPIView):
    queryset = models.Student.objects.all()
    serializer_class = StudentSerializer


@csrf_exempt
def student_login(request):
    email = request.POST['email']
    password = request.POST['password']
    try:
        studentExist = models.Student.objects.get(email=email, password=password)
        if studentExist:
            print(studentExist.id, "id")
            return JsonResponse({
                'bool': True,
                'full_name': studentExist.full_name,
                'id': studentExist.id,
                'email': studentExist.email
            })
    except ObjectDoesNotExist:
        return JsonResponse({
            'bool': False
        })


class StudentEnrollList(generics.ListCreateAPIView):
    queryset = models.StudentCourseEnrollment.objects.all()
    serializer_class = StudentEnrollSerializer


def studentEnrollStatus(request, student_id, course_id):
    course = models.Course.objects.filter(id=course_id).first()
    student = models.Student.objects.filter(id=student_id).first()
    enrollStatus = models.StudentCourseEnrollment.objects.filter(course=course, student=student)
    if enrollStatus:
        return JsonResponse({"enrollStatus": True})
    else:
        return JsonResponse({"enrollStatus": False})


class StudentEnrollPerCourse(generics.ListAPIView):
    queryset = models.StudentCourseEnrollment.objects.all()
    serializer_class = StudentEnrollPerCourseSerializer

    def get_queryset(self):
        if 'course_id' in self.kwargs:
            course_id = self.kwargs['course_id']
            course = models.Course.objects.get(pk=course_id)
            data = models.StudentCourseEnrollment.objects.filter(course=course)
            return data
        if 'teacher_id' in self.kwargs:
            teacher_id = self.kwargs['teacher_id']
            teacher = models.Teacher.objects.get(pk=teacher_id)
            return models.StudentCourseEnrollment.objects.filter(course__teacher=teacher).distinct()
        if 'student_id' in self.kwargs:
            student_id = self.kwargs['student_id']
            student = models.Student.objects.get(pk=student_id)
            return models.StudentCourseEnrollment.objects.filter(student=student).distinct()


class CourseRating(generics.ListCreateAPIView):
    serializer_class = CourseRatingSerializer
    queryset = models.CourseRating.objects.all()

    # def get_queryset(self):
    #     course_id = self.kwargs['course_id']
    #     course = models.Course.objects.get(pk=course_id)
    #     return models.CourseRating.objects.filter(course=course)


def studentRatingStatus(request, course_id, student_id):
    course = models.Course.objects.filter(id=course_id).first()
    student = models.Student.objects.filter(id=student_id).first()
    enrollStatus = models.CourseRating.objects.filter(course=course, student=student)
    if enrollStatus:
        return JsonResponse({"ratingStatus": True})
    else:
        return JsonResponse({"ratingStatus": False})


@csrf_exempt
def intructor_change_password(request, teacher_id):
    password = request.POST['password']
    try:
        instructorExist = models.Teacher.objects.get(id=teacher_id)
        if instructorExist:
            models.Teacher.objects.filter(id=teacher_id).update(password=password)
            return JsonResponse({
                'bool': True,
                'message': 'Password updated successfully'
            })
    except ObjectDoesNotExist:
        return JsonResponse({
            'bool': False,
            'message': 'user does not exists'
        })


class InstructorDashboardView(generics.RetrieveAPIView):
    queryset = models.Teacher.objects.all()
    serializer_class = InstructorDashboardSerializer


class RecommendedCourses(generics.ListAPIView):
    queryset = models.Course.objects.all()
    serializer_class = AllCourseSerializer

    def get_queryset(self):
        if 'student_id' in self.kwargs:
            student_id = self.kwargs['student_id']
            student = models.Student.objects.get(pk=student_id)
            interests = student.interests.split(',')
            query = Q()
            for interest in interests:
                query |= Q(technologies__icontains=interest)
            queryset = models.Course.objects.filter(query)

        return queryset


class FavoriteCoursesList(generics.ListCreateAPIView):
    serializer_class = FavoriteCourseSerializer
    queryset = models.FavoriteCourses.objects.all()

    def get_queryset(self):
        if 'student_id' in self.kwargs:
            student_id = self.kwargs['student_id']
            student = models.Student.objects.get(pk=student_id)
            return models.FavoriteCourses.objects.filter(student=student).distinct()


def CheckFavouriteCourseStatus(request, course_id, student_id):
    course = models.Course.objects.filter(id=course_id).first()
    student = models.Student.objects.filter(id=student_id).first()
    favoriteStatus = models.FavoriteCourses.objects.filter(course=course, student=student)
    if favoriteStatus:
        return JsonResponse({"favouriteStatus": True})
    else:
        return JsonResponse({"ratingStatus": False})


def removeFromFavoriteList(request, course_id, student_id):
    course = models.Course.objects.filter(id=course_id).first()
    student = models.Student.objects.filter(id=student_id).first()
    favoriteStatus = models.FavoriteCourses.objects.filter(course=course, student=student).delete()
    if favoriteStatus:
        return JsonResponse({"RemoveStatus": True})
    else:
        return JsonResponse({"RemoveStatus": False})


class StudentAssignmentList(generics.ListCreateAPIView):
    queryset = models.StudentAssignment.objects.all()
    serializer_class = StudentAssignmentSerializer

    def get_queryset(self):
        if 'student_id' and 'teacher_id' in self.kwargs:
            student_id = self.kwargs['student_id']
            teacher_id = self.kwargs['teacher_id']
            student = models.Student.objects.get(pk=student_id)
            teacher = models.Teacher.objects.get(pk=teacher_id)
            return models.StudentAssignment.objects.filter(student=student, teacher=teacher)
        elif 'student_id' in self.kwargs:
            student_id = self.kwargs['student_id']
            student = models.Student.objects.get(pk=student_id)
            return models.StudentAssignment.objects.filter(student=student)


class UpdateAssignment(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.StudentAssignment.objects.all()
    serializer_class = StudentAssignmentSerializer
