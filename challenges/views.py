from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

# Create your views here.
monthly_challenges = {
    'january':'todo challenge of january',
    'february': 'todo challenge for february',
    'march': 'todo challenge for march',
    'april': 'todo challenge for april',
    'may': 'todo challenge for may',
}

def index(request):
    return HttpResponse("This works")

def monthly_challenge(request, month):
    return HttpResponse(monthly_challenges.get(month))


def monthly_challenge_by_num(request, month):
    string_month = list(monthly_challenges.keys())[month-1]
    redirect_path = reverse('str_path', args=[string_month])
    return HttpResponseRedirect(redirect_path)

    