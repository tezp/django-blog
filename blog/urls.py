from django.urls import path

from blog.views import PostUpdateView, PostDeleteView
from .views import PostListView, PostDetailView, PostCreateView
from .views import home, about

urlpatterns = [
    # path('', home, name='home'),
    path('', PostListView.as_view(), name='home'),
    path('about', about, name='about'),
    path('posts/<int:pk>', PostDetailView.as_view(), name='post-detail'),
    path('posts/create', PostCreateView.as_view(), name='post-create'),
    path('posts/<int:pk>/update', PostUpdateView.as_view(), name='post-update'),
    path('posts/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'),

]
