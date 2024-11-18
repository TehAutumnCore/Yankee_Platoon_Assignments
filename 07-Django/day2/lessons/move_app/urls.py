from django.urls import path
from .views import AllMoves, Single_move

urlspatterns = [
    path('',Allmoves.as_view(), name='all_moves'),
    path('<str:single_move>', single_move.as_view(),name='single_move')
]