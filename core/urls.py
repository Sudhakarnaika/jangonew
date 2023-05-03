from django.urls import path
from .views import Home
from .views import Home, Add_Student,Delete_Student,EditStudent

urlpatterns = [
    path('', Home.as_view(), name = 'home'),
    path('Add_Student/', Add_Student.as_view(), name = 'add-student'),
    path('Delete_Student/', Delete_Student.as_view(), name = 'delete-student'),
    path('EditStudent/<int:id>/', EditStudent.as_view(), name = 'edit-student')
]



