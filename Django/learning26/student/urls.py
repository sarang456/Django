from django.urls import path
from.import views
urlpatterns = [
    path('home/', views.studenthome),
    path("Studentdash/", views.student_dashbord),
    path("notification/", views.noti),
    path("scholership/", views.scholer),
    path("useful-links/", views.useful)
]