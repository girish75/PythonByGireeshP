# This page shows what we want to show to our Website users.
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
import django.urls
from django.template.loader import render_to_string
from django.urls import reverse
challeng = {
    "january": "Walk at least 5000 Steps a day",
    "february": "Walk at least 6000 Steps a day and eat more vagitables",
    "march": "Walk at least 5000 Steps a day",
    "april": "Walk at least 6000 Steps a day and eat more vagitables",
}


# Create your views here.
def challenges_home(request):
    list_items = ""
    months = list( challeng.keys())
    for month in months:
        print(month)
        capitalized_month = month.capitalize()
        month_path = django.urls.reverse( "str_path_identifier", args=[month] )
        list_items += f"<li><a href = \" {month_path}\"> {capitalized_month }</a></li>"

    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse( response_data)


def monthly_challenge_bynumber(request, month):
    if month > len( challeng ):
        return HttpResponseNotFound( "<h1>Invalid month entered</h>" )

    months = list( challeng.keys() )
    redirect_month = months[month - 1]
    redirect_path = django.urls.reverse( "str_path_identifier", args=[redirect_month] )  # /challenge/enteredmonth
    # "str_path_identifier" is the name given in urls file for a path to this app challenge
    # return HttpResponseRedirect("/challenges/"+ redirect_month)
    return HttpResponseRedirect( redirect_path )


# def monthly_challenge(request, month):
#     print( f"request ={request} and month is = {month}" )
#     #try:
#     challenge_text = challeng[month]
#     response_data = render_to_string("challenges/challenge.html")
#     return HttpResponse(response_data)
#     #return render(request,"challenges/challenge.html", {
#        # "text": challenge_text})# user Django templates language
#
#     # response_data = f"<H1>{challenge_text}</H1>"
#
#     # print(challenge_text)
#     # return HttpResponse(challenge_text)
#     #2 return HttpResponse( f"{month} page! \n  {response_data}" )
#     # if month.upper() == 'JAN':
#     #     challenge_text= f"Laugh more in {month}"
#     # elif month.upper() == 'FEB':
#     #     challenge_text = f"Workout more in {month}"
#     # else:
#     #     challenge_text = "This month enjoy!!!"
# #except:
#    #return HttpResponseNotFound( "<h1>This month is not supported</h>" )

def monthly_challenge(request, month):
#     try:
        challenge_text = challeng[month]
        return render(request, "challenge.html", {
            "text": challenge_text,
            "month_name": month.capitalize()
        })
#
#     except:
#         return HttpResponseNotFound("<h1>This month is not supported </h1>")
