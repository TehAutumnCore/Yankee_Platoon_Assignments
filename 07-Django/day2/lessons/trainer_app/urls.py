from django.urls import path
from .views import SignUp,LogOut,LogIn, Info, AdminUser

urlpatterns=[
    #signup
    path('signup/', SignUp.as_view(), name='signup'),
    #logout
    path('logout/', LogOut.as_view(), name='logout'),
    #login
    path('login/', LogIn.as_view(), name='login'),
    #info of user
    path('info/', Info.as_view(), name='info'),
    #admin user - superuser
    path('admin-user/',AdminUser.as_view(), name='admin user')
]