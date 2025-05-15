from django.urls import path
from . import views

urlpatterns = [
    path("", views.acceuil, name="acceuil" ),
    path("comment/", views.comment, name="comment" ),
    path("thank_you/", views.thank_you1.as_view(), name="sucess"),
    path("theses/",views.theses, name="theses"),
    path("theses/<slug:slug>/", views.thesis_detail, name="thesis_details"),
    path("projects/", views.projects, name="projects"),
    path("projects/<slug:slug>/", views.project_detail, name="project_details")
    
]
