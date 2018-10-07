from django.shortcuts import render

# Create your views here.
from main.models import ChoiceInfo


def index(request):
    return render(request, 'main/index.html')


def exam(request):
    right_num = request.session.get('right_num',0)

    question_id = request.POST.get("question_id")
    answer = request.POST.get("answer")


    objs = ChoiceInfo.objects.all()


    if question_id:

        choiceInfo_last = objs.filter(question_id=question_id).first()

        if choiceInfo_last.answer == int(answer):
            right_num = right_num + 1
            request.session['right_num'] = right_num

        choiceInfo = objs.filter(question_id__gt=question_id).first()

        if choiceInfo is None:
            all = ChoiceInfo.objects.count()
            score = round((float(right_num) / float(all) * 100))

            print(score)

            return render(request, 'main/result.html',{"score": score})

    else:

        choiceInfo = objs.filter(question_id=1).first()
        request.session['right_num'] = 0

    return render(request, 'main/exam.html', {"choiceInfo": choiceInfo})

