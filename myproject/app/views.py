from django.shortcuts import render
from django.http import JsonResponse
from datetime import datetime
from django.db import connection

mycursor = connection.cursor()

def map(request):
    return render(request, "map.html")

def restaurant(request):
    item_range = range(1, 5)
    return render(request, "restaurant.html", {"item_range": item_range})

def comments(request):
    comment_range = range(5)
    return render(request, "comments.html", {"comment_range": comment_range})

def compile(request):
    return render(request, "compile.html")

def login(request):
    return render(request, "login.html")

def signup(request):
    return render(request, "signup.html")

def signupadd(request):
    username = request.POST['username']
    email = request.POST['email']
    pwd = request.POST['pwd']
    pwdcf = request.POST['pwdcf']
    print(username, email, pwd, pwdcf)
    mycursor.execute('insert into userinfo(userID, username, password, truename) values(%s, %s, %s, %s)',
                     (2, username, pwd, username))
    return render(request, "signupadd.html")

def userlist(request):
    mycursor.execute('select * from userinfo')
    usersinfo = mycursor.fetchall()
    head = [head[0] for head in mycursor.description]
    users = []
    for user in usersinfo:
        output = zip(head, user)
        # print(dict(output))
        users.append(dict(output))
    return render(request, "userlist.html", {'userlist': users, 'head': head})
