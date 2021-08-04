from django.urls import path 
from .views import BlogView,PostDetailView,PostCreateView,PostEditView,PostDeleteView

urlpatterns = [
    path('post/<int:pk>/delete',PostDeleteView.as_view(),name='post_delete'),
    path('post/<int:pk>/update',PostEditView.as_view(),name='post_edit'),
    path('post/new/',PostCreateView.as_view(),name='new_blog'),
    path('post/<int:pk>/',PostDetailView.as_view(),name='post_detail'),
    path('',BlogView.as_view(),name='home')
]
