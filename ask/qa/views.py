from django.core.paginator import Paginator, EmptyPage
from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_GET, require_POST

from forms import AnswerForm, AskForm
from models import Question, Answer


def test(request, *args, **kwargs):
    return HttpResponse('OK')


@require_GET
def home(request):
    questions = Question.objects.order_by('id')
    paginator, page = paginate(request, questions)

    return render(request, 'qa/home.html', {
        'questions': page.object_list,
        'paginator': paginator,
        'page': page,
    })


@require_GET
def popular(request):
    questions = Question.objects.order_by('-rating')
    paginator, page = paginate(request, questions)

    return render(request, 'qa/popular.html', {
        'questions': page.object_list,
        'paginator': paginator,
        'page': page,
    })


@require_GET
def question(request, id):
    question = get_object_or_404(Question, pk=id)
    answers = Answer.objects.filter(question_id__exact=int(id))
    answer_form = AnswerForm({"question": question.id})

    return render(request, 'qa/question.html', {
        'question': question,
        'answers': answers,
        'form': answer_form
    })


@require_POST
def answer(request):
    form = AnswerForm(request.POST)
    if form.is_valid():
        answer = form.save(commit=False)
        answer.author = request.user
        answer.save()
        return redirect(answer.question)


def ask(request):
    if request.method == "POST":
        form = AskForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user
            question.save()
            return redirect(question)
    else:
        form = AskForm()
    return render(request, 'qa/ask.html', {'form': form})


def paginate(request, qs):
    try:
        limit = int(request.GET.get('limit', 10))
    except ValueError:
        limit = 10

    if limit > 100:
        limit = 10

    try:
        page = int(request.GET.get('page', 1))
    except ValueError:
        raise Http404

    paginator = Paginator(qs, limit)
    try:
        page = paginator.page(page)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)

    return paginator, page


