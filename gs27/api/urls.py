from django.urls import path
from api import views
urlpatterns =[
    path('stucreate/', views.StudentListCreate.as_view()),
    path('stucreate/<int:pk>', views.StudentRetrieveUpdateDestroy.as_view()),
]