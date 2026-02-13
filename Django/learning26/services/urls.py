from django.urls import path
from .import views

urlpatterns = [
    path("service_list/", views.service_list, name = "list"),
    path("create_service/", views.create_service, name="create"),
    path("service_update/ <id>", views.service_update, name="update"),
    path("service_delete/ <id>", views.service_delete, name="delete")
]