from django.shortcuts import render,HttpResponse,redirect
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

def map_(request):
    mycursor.execute('select * from Restaurant')
    restaurants_info = mycursor.fetchall()
    
    restaurants = []
    restaurant_head = [head[0] for head in mycursor.description]
    for restaurant_info in restaurants_info:
        merge = zip(restaurant_head, restaurant_info)
        restaurants.append(dict(merge))

    return render(request, "map.html", {"restaurants": restaurants,})

def restaurant_(request):
    Rid = request.GET['Rid']
    mycursor.execute('select * from Restaurant where Rid = %s', (Rid,))
    restaurant_info = mycursor.fetchall()[0]
    restaurant_head = [head[0] for head in mycursor.description]

    merge = zip(restaurant_head, restaurant_info)
    restaurant = dict(merge)

    return render(request, "restaurant.html", {"restaurant": restaurant,})

def comments_(request):
    comment_range = range(5)

    # restaurant
    Rid = request.GET['Rid']
    mycursor.execute('select * from Restaurant where Rid = %s', (Rid,))
    restaurant_info = mycursor.fetchall()[0]
    restaurant_head = [head[0] for head in mycursor.description]

    merge = zip(restaurant_head, restaurant_info)
    restaurant = dict(merge)

    # comment
    mycursor.execute('select * from Comment where Rid = %s', (Rid,))
    comments_info = mycursor.fetchall()
    comment_head = [head[0] for head in mycursor.description]

    comments = []
    for comment_info in comments_info:
        merge = zip(comment_head, comments_info)
        comments.append(dict(merge))

    return render(request, "comments.html", {"comments": comments, "restaurant": restaurant,})



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
    mycursor.execute('select * from userinfo limit 1')
    users_info = mycursor.fetchall()
    user_head = [head[0] for head in mycursor.description]
    users = []
    # print(users_info)
    for user in users_info:
        merge = zip(user_head, user)
        users.append(dict(merge))
    print(users)
    return render(request, "userlist.html", {'userlist': users, 'head': head})
