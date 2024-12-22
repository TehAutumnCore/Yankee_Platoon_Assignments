from django.urls import path
from .views import LibraryViewAll, LibraryViewDelete

urlpatterns = [
    path('', LibraryViewAll.as_view(), name='library-list'),
    path('<int:id>/delete/', LibraryViewDelete.as_view(), name='library-delete'),
]