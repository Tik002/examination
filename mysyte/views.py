from .models import Lecture, Course
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate

# Create your views here.

def index(request):
    course = Course.objects.all()
    return render(request, "mysyte/index.html", {"course": course})

def detail(request, pk):
    course = get_object_or_404(Course, pk=pk)
    return render(request, "mysyte/details.html", {"course": course})

# def rate(request, question_id):
#     course = get_object_or_404(Course, pk=question_id)
#     try:
#         selected_choice = course.choice_set.get(pk=request.POST["choice"])
#     except (KeyError, Choice.DoesNotExist):
#         return render(
#             request,
#             "polls/detail.html",
#             {
#                 "course": course,
#                 "error_message": "You didn't select a choice.",
#             },
#         )
#     else:
#         selected_choice.votes = F("votes") + 1
#         selected_choice.save()
#         return HttpResponseRedirect(reverse("polls:results", args=(course.id,)))

def add(request):
    if request.user.is_authenticated:
        if request.method == 'GET':
            return render(request, "mysyte/add.html")
        
        else:
            title = request.POST.get('title')
            user = request.user
            ru = get_object_or_404(Lecture, user=user)
            description= request.POST.get('description')
            course = Course(
                        title = title,
                        description = description,
                        creator=ru
                        )
            course.save()
            return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect("/login/")

def log_in(request):
    if request.method == "GET":
            return render(request, "mysyte/login.html", {})
        
    usr = request.POST['username']
    pswd = request.POST['password']
    
    user = authenticate(username=usr, password=pswd)
    if user:
        login(request, user)
        return HttpResponseRedirect("/")
        
    return render(request, "recipes/login.html", {"error": "username or password is wrong"})

def log_out(request):
    logout(request)
    return HttpResponseRedirect("login")

def register(request):
    if request.method == 'GET':
        return render(request, 'mysyte/register.html')
    
    firstname = request.POST['fname']
    lastname = request.POST['lname']
    username = request.POST['username']
    age = request.POST['age']
    email = request.POST['email']
    password = request.POST['password']
    user = User.objects.create_user(
                first_name = firstname, 
                last_name = lastname, 
                username = username,
                password = password,
                email = email)
    user.save()
    recipesuser = Lecture(user = user, age = age)
    recipesuser.save()
    return HttpResponseRedirect('/login/')