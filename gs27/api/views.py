#We have to test this API through Browser
from api.models import Student
from .serializers import StudentSerializer
from rest_framework.generics import ListAPIView
from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView

# Create your views here.
#To GET all data(List)   and   To POST data(Create)
class StudentListCreate(ListCreateAPIView): #pk(primary key is not required)
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

    def get_queryset(self): #This function is used to filter data for specific user
        user=self.request.user
        return Student.objects.filter(teacher=user)

#To GET specific data(Retrieve)   and   To PUT/PATCH data(Update)   and   To DELETE data(Destroy)
class StudentRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView): #pk(Primary key is required)
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

    def get_queryset(self): #This function is used to filter data for specific user
        user=self.request.user #in //request.user// we have always current user
        return Student.objects.filter(teacher=user)



# class StudentListCreate(ListAPIView): #pk(primary key is not required)
#     queryset=Student.objects.all()
#     serializer_class=StudentSerializer
#     def get_queryset(self):
#         user=self.request.user
#         return Student.objects.filter(teacher=user)