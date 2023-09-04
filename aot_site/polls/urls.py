from django.urls import path
from . import views

app_name = 'polls'

urlpatterns = [

    # index to register / login  to home
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('home/', views.home, name='home'),

    # poll functionality : voting, detail and result views.
    path('home/polls/', views.polls, name='polls'),
    path('home/polls/<int:question_id>/', views.detail, name='detail'),
    path('home/polls/<int:question_id>/results/', views.result, name='result'),
    path('home/polls/<int:question_id>/vote/', views.vote, name='vote'),

    # store
    path('home/store/', views.store, name='store')
]
