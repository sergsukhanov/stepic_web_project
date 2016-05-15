from django.core.paginator import Paginator, EmptyPage
from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_GET, require_POST

from forms import AnswerForm, AskForm
from models import Question, Answer


def test(request, *args, **kwargs):
    return HttpResponse('OK')


