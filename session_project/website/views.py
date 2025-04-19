from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect


def cookie_session(request):
    request.session.set_test_cookie()
    return HttpResponse("<h1>dataflair</h1>")


def cookie_delete(request):
    if request.session.test_cookie_worked():
        request.session.delete_test_cookie()
        return HttpResponse("dataflair<br>cookie created")
    else:
        return HttpResponse("Dataflair<br>Your browser does not accept cookies")


def create_session(request):
    request.session["name"] = "Saveliy"
    request.session["password"] = "password123"
    return HttpResponse("<h1>dataflair<br>the session is set</h1>")


def access_session(request):
    response = "<h1>Welcome to Sessions of dataflair</h1><br>"
    if request.session.get("name"):
        response += f"Name : {request.session.get('name')} <br>"
    if request.session.get("password"):
        response += f"Password : {request.session.get('password')} <br>"
        return HttpResponse(response)
    else:
        return redirect("/create/")


def delete_session(request):
    try:
        del request.session["name"]
        del request.session["password"]
    except KeyError:
        pass
    return HttpResponse("<h1>dataflair<br>Session Data cleared</h1>")
