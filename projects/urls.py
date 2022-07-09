from django.urls import path
from . import views

urlpatterns = [
    path('', views.projects, name="projects"),
    path('projectview/<str:pk>/', views.project, name="project"),
    path('project/create-project/',views.createProject, name="create-project"),
    path('project/update-project/<str:pk>/',views.updateProject, name="update-project"),

    path('project/delete-project/<str:pk>/',views.deleteProject, name="delete-project")
]
