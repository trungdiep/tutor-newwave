from django.urls import path
from .views import plan_course
urlpatterns = [
    path("plan-course", plan_course)
]