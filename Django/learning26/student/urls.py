from django.urls import path
from.import views
app_name = "student"

urlpatterns = [
    path('home/', views.studenthome),
    path("Studentdash/", views.student_dashbord),
    path("notification/", views.noti),
    path("scholership/", views.scholer),
    path("useful-links/", views.useful),
    path("servicelist/", views.service_list, name="list"),
    path("createservice/", views.service_create, name="create"),
    path("updateservice/<int:id>", views.service_update, name="update"),
    path("deleteservice/<int:id>", views.service_delete, name ="delete")
]