from django.urls import path, re_path
from host import views

urlpatterns = [
    path('hosts', views.HostModelViewSet.as_view({"get": "list", "post": "create"})),
    re_path('(?P<pk>\d+)', views.HostModelViewSet.as_view({"get": "retrieve", "delete": "destroy"})),
    path('category', views.HostCategoryListAPIView.as_view()),
    path('excel_host', views.HostExcelView.as_view()),
    path("search/", views.HostModelViewSet.as_view({"get": "search"})),
]
