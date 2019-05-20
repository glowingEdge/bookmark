from django.urls import path
from .views import BookmarkListView, BookmarkCreateView, BoookmarkDetailView


urlpatterns = [
    path('', BookmarkListView.as_view(), name='list'),
    path('add/', BookmarkCreateView.as_view(), name='add'),
    path('detail/<int:pk>/', BoookmarkDetailView.as_view(), name='detail'),
]