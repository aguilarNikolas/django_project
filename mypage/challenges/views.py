from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, Http404
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
    "december": None,
}

def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())
    return render(request, "challenges/index.html",{
        "months":months
    })


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
        return render(request, "challenges/challenge.html",{
            "text": challenge_text,
            "month_name": month,
        })

    except:
       raise Http404()
    

