from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views import View
from .models import *
from quizapp.models import Quiz, Savol, Javob

class QuizSaveView(View):
    def post(self, request, pk):
                if request.is_ajax():
                    questions = []
                    data = request.POST
                    data_ = dict(data.lists())

                    data_.pop('csrfmiddlewaretoken')

                    for k in data_.keys():
                        print('key: ', k)
                        question = Savol.objects.get(matn=k)
                        questions.append(question)

                    user = request.user
                    quiz = Quiz.objects.get(id=pk)

                    score = 0
                    marks = []
                    correct_answer = None

                    for q in questions:
                        a_selected = request.POST.get(q.matn)

                        if a_selected != "":
                            question_answers = Javob.objects.filter(savol=q)
                            for a in question_answers:
                                if a_selected == a.matn:
                                    if a.togri:
                                        score += 1
                                        correct_answer = a.matn
                                else:
                                    if a.togri:
                                        correct_answer = a.matn

                            marks.append({str(q): {'correct_answer': correct_answer, 'answered': a_selected}})
                        else:
                            marks.append({str(q): 'not answered'})

                    Foydalanuvchi.objects.create(quiz=quiz, user=user, baho=score)

                    return JsonResponse({'passed': True, 'score': score, 'marks': marks})
class ResultView(View):
    def get(self, request):
        marks = Foydalanuvchi.objects.all()
        return render(request, 'results.html', {'marks': marks})


class Delete_resultView(View):
    def get(self, request, son):
        marks = Foydalanuvchi.objects.get(id=son)
        return render(request, 'delete_result.html', {'marks': marks})

    def post(self, request, son):
        if request.user.is_authenticated:
            marks = Foydalanuvchi.objects.get(id=son)
            marks.delete()
            return redirect('/result')
        else:
            return redirect('/result')





