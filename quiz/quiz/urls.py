from django.contrib import admin
from django.urls import path

from quizapp.views import QuizView, IndexView, Add_OptionView, Add_QuestionView, Add_QuizView, BaseView,\
       Delete_QuestionView,  QuizDataView, SignupView, LoginView, Delete_QuizView

from natijaapp.views import ResultView,  QuizSaveView, Delete_resultView

from quizapp.views import LogOut

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('<int:pk>/', QuizView.as_view(), name='quiz'),
    path('<int:pk>/data/', QuizDataView.as_view(), name='quizdata'),

    path('add_options/<int:son>/', Add_OptionView.as_view(), name='addop'),
    path('add_question/', Add_QuestionView.as_view(), name='addques'),
    path('add_quiz/', Add_QuizView.as_view(), name='addquiz'),

    path('base/', BaseView.as_view(), name='base'),

    path('delete_question/<int:son>/', Delete_QuestionView.as_view(), name='delques'),
    path('delete_result/<int:son>/', Delete_resultView.as_view(), name='delresult'),
    path('delete_quiz/<int:son>/', Delete_QuizView.as_view(), name='delquiz'),


    path('<int:pk>/save/', QuizSaveView.as_view(), name='quizsave'),
    path('result/', ResultView.as_view(), name='result'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogOut, name='logout'),

]
