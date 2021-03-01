from django.urls import path
from . import views

urlpatterns = [
    
    path('',views.index,name='index'),
    path('login/',views.login,name='login'),
    path('register/',views.register,name='register'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('logout/',views.logout,name='logout'),
    path('manage_users/',views.manage_users,name='manage_users'),
    path('manage_questions/',views.manage_questions,name='manage_questions'),
    path('delete_user/<pk>',views.delete_user,name='delete_user'),
    path('change_password/',views.change_password,name='change_password'),
    path('add_question/',views.add_question, name='add_question'),
    path('delete_question/<pk>',views.delete_question,name='delete_question'),
    path('Edit_questions/<pk>',views.Edit_questions,name='Edit_questions'),
    path('Update/',views.Update,name='Update'),
    path('edit_user/<pk>',views.edit_user,name='edit_user'),
    path('update_user/',views.update_user,name='update_user'),
    path('quiz/',views.quiz,name='quiz'),
    #path('total_question/',views.total_question,name='total_question'),
    #path('total_user/',views.total_user,name='total_user'),
    #path('result/',views.result,name='result'),
]
