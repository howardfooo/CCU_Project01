from django.shortcuts import render,HttpResponse,redirect
from django.http import JsonResponse
from datetime import datetime
from django.db import connection
import base64

mycursor = connection.cursor()

def login(request):
    return render(request, "login.html")

def signup(request):
    return render(request, "signup.html")

def map(request):
    mycursor.execute('select * from Restaurant')
    restaurants_info = mycursor.fetchall()
    
    restaurants = []
    restaurant_head = [head[0] for head in mycursor.description]
    for restaurant_info in restaurants_info:
        merge = zip(restaurant_head, restaurant_info)
        restaurant = dict(merge)
        agree = [i for i in range(restaurant['rate'])]
        disagree = [i for i in range(5-restaurant['rate'])]
        restaurant['rate'] = (agree, disagree)
        restaurants.append(restaurant)
        

    return render(request, "map.html", {"restaurants": restaurants,})

def restaurant(request):
    Rid = request.GET['Rid']
    UserID = 1

    # restaurant
    mycursor.execute('select * from Restaurant where Rid = %s', (Rid,))
    restaurant_info = mycursor.fetchall()[0]
    restaurant_head = [head[0] for head in mycursor.description]
    
    merge = zip(restaurant_head, restaurant_info)
    restaurant = dict(merge)
    agree = [i for i in range(restaurant['rate'])]
    disagree = [i for i in range(5-restaurant['rate'])]
    restaurant['rate'] = (agree, disagree)
    restaurant['menu'] = base64.b64encode(restaurant['menu']).decode('utf-8')

    # type
    mycursor.execute('select distinct dishtype from Dish where Rid=%s', (Rid,))
    dishes_type_info = mycursor.fetchall()
    dishes_type=[i[0] for i in dishes_type_info]

    # dish + type
    dishes_all = []
    for type in dishes_type:
        mycursor.execute('select * from Dish where dishtype = %s', (type,))
        dishes_info = mycursor.fetchall()
        dish_head = [head[0] for head in mycursor.description]
        dishes = []
        for dish_info in dishes_info:
            merge = zip(dish_head, dish_info)
            dish = dict(merge)
            if (dish['image'] != None):
                dish['image'] = base64.b64encode(dish['image']).decode('utf-8')
            else:
                dish['image'] = 0
            dishes.append(dish)
        dishes_all.append({type: dishes})
    
    # ifFav
    mycursor.execute('select COUNT(*) from Fav where Rid=%s and UserID=%s', (Rid, UserID))
    ifFav = mycursor.fetchall()[0][0]
    print(ifFav)

    return render(request, "restaurant.html", {"restaurant": restaurant, "dishes_all": dishes_all, "ifFav": ifFav})

def restaurant_fav(request):
    Rid = request.GET['Rid']
    UserID = 1
    mycursor.execute('select COUNT(*) from Fav where UserID = %s and Rid = %s', (UserID, Rid))
    if mycursor.fetchone()[0] == 0:
        path = '/restaurant?Rid={}'.format(Rid)
        mycursor.execute('insert into Fav(UserID, Rid, date) values(%s, %s, %s)', (UserID, Rid, '2024-06-12'))
    else:
        # 你已加入最愛
        path = '/favorite'

    return redirect(path)

def comments(request):
    comment_range = range(5)
    Rid = request.GET['Rid']

    # restaurant
    mycursor.execute('select * from Restaurant where Rid = %s', (Rid,))
    restaurant_info = mycursor.fetchall()[0]
    restaurant_head = [head[0] for head in mycursor.description]
    
    merge = zip(restaurant_head, restaurant_info)
    restaurant = dict(merge)
    agree = [i for i in range(restaurant['rate'])]
    disagree = [i for i in range(5-restaurant['rate'])]
    restaurant['rate'] = (agree, disagree)
    restaurant = restaurant

    # comment
    mycursor.execute('select * from Comment where Rid = %s', (Rid,))
    comments_info = mycursor.fetchall()
    comment_head = [head[0] for head in mycursor.description]

    comments = []
    for comment_info in comments_info:
        merge = zip(comment_head, comment_info)
        comment = dict(merge)

        # 星星
        agree = [i for i in range(comment['rate'])]
        disagree = [i for i in range(5-comment['rate'])]
        comment['rate'] = (agree, disagree)

        # 大頭貼
        mycursor.execute('select photo from Users where UserID = %s', (comment['UserID'],))
        photo = mycursor.fetchall()[0][0]
        comment['photo'] = base64.b64encode(photo).decode('utf-8')

        # 照片
        mycursor.execute('select image from Comment_img where UserID=%s and time=%s', (comment['UserID'], comment['time']))
        images_raw = mycursor.fetchall()
        images = []
        for image in images_raw:
            images.append(base64.b64encode(image[0]).decode('utf-8'))
        comment['images'] = images

        # 影片
        if comment['video'] != None:
            comment['video'] = base64.b64encode(comment['video']).decode('utf-8')
        else:
            comment['video'] = 0

        # Tag
        mycursor.execute('select tag, Rid from Tag where UserID=%s and time=%s', (comment['UserID'], comment['time']))
        tags_info = mycursor.fetchall()
        tag_head = [head[0] for head in mycursor.description]
        tags = []
        for tag_info in tags_info:
            merge = zip(tag_head, tag_info)
            tags.append(dict(merge))
        
        for tag in tags:
            mycursor.execute('select color from Dish where Dname=%s and Rid=%s', (tag['tag'], tag['Rid']))
            color = mycursor.fetchall()[0][0]
            print(color)
            tag['color'] = color
        print(tags)
        
        comment['tags'] = tags
        comments.append(comment)

    return render(request, "comments.html", {"comments": comments, "restaurant": restaurant,})

def compile(request):
    Rid = request.GET['Rid']

    # restaurant
    mycursor.execute('select * from Restaurant where Rid = %s', (Rid,))
    restaurant_info = mycursor.fetchall()[0]
    restaurant_head = [head[0] for head in mycursor.description]
    
    merge = zip(restaurant_head, restaurant_info)
    restaurant = dict(merge)
    agree = [i for i in range(restaurant['rate'])]
    disagree = [i for i in range(5-restaurant['rate'])]
    restaurant['rate'] = (agree, disagree)

    return render(request, "compile.html", {"restaurant": restaurant,})

def favorite(request):
    UserID = 1
    mycursor.execute('select Rid, Date from Fav where UserID = %s', (UserID,))
    adds_info = mycursor.fetchall()
    add_head = [head[0] for head in mycursor.description]
    adds = []
    for add_info in adds_info:
        merge = zip(add_head, add_info)
        adds.append(dict(merge))

    restaurants = []
    for add in adds:
        mycursor.execute('select * from Restaurant where Rid = %s', (add['Rid'],))
        restaurant_info = mycursor.fetchall()[0]
        restaurant_head = [head[0] for head in mycursor.description]

        merge = zip(restaurant_head, restaurant_info)
        restaurant = dict(merge)
        restaurant['date'] = add['date']
        restaurant['image'] = base64.b64encode(restaurant['image']).decode('utf-8')
        restaurants.append(restaurant)

    return render(request, "favorite.html", {"restaurants": restaurants,})

def favorite_del(request):
    Rid = request.GET['Rid']
    back = request.GET['back']
    UserID = 1
    mycursor.execute('delete from Fav where Rid = %s and UserID = %s', (Rid, UserID))
    if (back == 'restaurant'):
        return redirect('/restaurant?Rid='+Rid)
    return redirect('/favorite')