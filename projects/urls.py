from django.urls import path
from . import views

app_name = 'projects'

urlpatterns = [
    path('list/', views.project_list, name='project_list'),
    path('create/', views.project_create, name='project_create'),
    path('<slug:slug>/', views.project_detail, name='project_detail'),
    path('<slug:slug>/update/', views.project_update, name='project_update'),
    path('<slug:slug>/delete/', views.project_delete, name='project_delete'),
    path('comment/<int:pk>/delete/', views.delete_comment, name='delete_comment'),
]