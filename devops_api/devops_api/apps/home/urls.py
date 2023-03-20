from django.urls import path
from home import views

urlpatterns = [
    path('', views.home),
    path('test', views.TestView.as_view()),
]
