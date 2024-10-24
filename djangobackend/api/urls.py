from django.urls import path
from .views import StudentList
from .views import FrameList

urlpatterns = [
    path('api/frameDataStorage', FrameList.as_view(), name='frame sets'),
    path('api/students', StudentList.as_view(), name='students'),
    path('api/delete/<int:idDelete>', StudentList.as_view(), name='delete'),
    path('api/update/<int:idUpdate>', StudentList.as_view(), name='update'),
]

