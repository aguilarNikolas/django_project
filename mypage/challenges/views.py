from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
# Create your views here.

monthly_challenges = {
    "january": "Eat a lot of meat",
    "february": "Walk for 20 minutes every day",
    "march": "Eat no meat for the entire month",
    "april": "hug a tree",
    "may": "Walk for 3 minutes every day",
    "june": "learn django",
    "july": "run 10km",
    "august": "walk 10km",
    "september": "eat no meat",
    "october": "eat meat",
    "november": "walk 15km",
    "december": "no meat",
}

def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())
    for month in months:
        redirect_path = reverse("month-challenge", args=[month])
        list_items += f"<li><a href=\"{redirect_path}\">{month.capitalize()}</a></li>"
    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("Invalid month")
    redirect_month = months[month-1]
    redirect_path = reverse("month-challenge", args=[redirect_month]) #will construct a url path dynamically
    return HttpResponseRedirect(redirect_path)

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        response_data = f"<h1>{challenge_text}</h1>"
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("<h1>This month is not supported</h1>")
    

