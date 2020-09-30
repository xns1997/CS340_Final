from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from django.db import connection

from MySQLdb import connect

from django.http import HttpResponseRedirect

# A test function to test data interaction between terminals and the databases
def link(statement=""):
    db = connect('classmysql.engr.oregonstate.edu', 'cs340_xuna', '9970', 'cs340_xuna')
    cursor=db.cursor()
    cursor.execute(statement)

# convert a data set from database to a data set for rendering 
def villager_converter(datas):
    # Helper functions to make empty input to be valid
    def cloth(num): 
        if num == None:
            return "NULL"
        else:
            return ""
    def per(num):
        if num == None:
            return "NULL"
        else:
            return per_list[num]

    def birth(str_birth):
        if str_birth == None:
            return "NULL"
        else:
            return str_birth

    def phrase(str_phrase):
        if str_phrase == None:
            return "NULL"
        else:
            return str_phrase
    def spice(num):
        if num == None:
            return "NULL"
        else:
            return species_list[num]
    species_list = ["Alligator","Anteater","Bear","Bird","Bull","Cat","Chicken",\
                    "Cow","Cub","Deer","Dog","Duck","Eagle","Elephant","Frog","Goat",\
                    "Gorilla","Hamster","Hippo","Horse","Kangaroo","Koala","Lion",\
                    "Monkey","Mouse","Octopus","Ostrich","Penguin","Pig","Rabbit",\
                    "Rhino","Sheep","Squirrel","Tiger","Wolf"]
    per_list = ["Lazy (Bonyari)","Jock (Hakihaki)","Cranky (Kowai)","Smug (Kiza)","Normal (Futsuu)","Peppy (Genki)","Snooty (Otona)","Sisterly (Aneki)"]
    result = {}
    for data in datas:
        # print(data)
        birth_str = birth(data[7]) if birth(data[7]) != "NULL" else "xx-xx"
        result[data[0]] = {"id":data[0],"name":data[1],"phrase":phrase(data[2]),"gender":data[3],"gender_num": data[3],"personality":per(data[4]),"per_num":data[4],"species":spice(data[5]), "sp_num":data[5],"cloth":cloth(data[6]),"birthday":birth(data[7]),"birth_str":birth_str, "edit":0}
        # print(result[data[0]])
    return result

# convert a data set from database to a data set for rendering 

def material_converter(datas):
    rare_list = ["NULL", "Very Common", "Common", "Rare", "Super Rare", "Seasonal", "Event Limited"]
    result = {}
    for data in datas:
        result[data[0]] = {"name":data[1],"rarity":rare_list[data[2]]}
    return result

# convert a data set from database to a data set for rendering 

def recipe_converter(datas):
    result = {}
    for data in datas:
        sql = "SELECT name FROM cs340_xuna.materials WHERE id = "
        sql += str(data[2]) + ";"
        print(sql)
        cursor = connection.cursor()
        cursor.execute(sql)
        material = cursor.fetchall()
        print(material[0][0])
        result[data[0]] = {"mat":material[0][0],"num":data[3]}
    return result

# convert a data set from database to a data set for rendering 

def furniture_converter(datas):
    source_list = ["Nook's Cranny", "DIY", "NOOK Miles", "NOOK Shopping", "Gulliver", "Fishing", "Bug-Off"]
    size_list  = ["1*1", "1*2", "1*3", "0.5*2", "2*2" ,"2*3", "3*3"]
    result = {}
    for data in datas:
        sql = "SELECT * FROM cs340_xuna.recipe_items WHERE fid = "
        sql += str(data[0]) + ";"
        cursor = connection.cursor()
        cursor.execute(sql)
        recipe = cursor.fetchall()
        # print(recipe)
        recipe = recipe_converter(recipe)
        print(recipe)
        result[data[0]] = {"name":data[1],"size":size_list[data[2]],"sold":data[3], "bought":data[4], "source": source_list[data[5]],"customizable":data[6],"recipe":recipe}
    return result

# To render the welcome page

def index(request):
    context          = {}
    context['hello'] = str(request.path)
    # print(render(request, 'index.html', context))
    print(request.path)
    return render(request, 'welcome.html', context)

# To render the villagers page

def villagers(request):
    print(request)
    context = {}
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM cs340_xuna.villagers")
    data = cursor.fetchall()
    data = villager_converter(data)
    context['data'] = data
    context['villager'] = 0
    return render(request,'villager.html',context)

# To make an ADD statement for new villager and send it to the database

def add_villager(request,name = "", gender = 0, species = 0,phrase = "" ,per = 9 , cloth = 0, birth = "xx-xx"):
    print(request)
    context = {}
    cursor = connection.cursor()
    sql = "INSERT INTO cs340_xuna.villagers (name"
    if name == "nah":
        name = "'no_name'"
    sql += ",gender"
    if species != 0:
        sql += ",species"
    if phrase != "nah":
        sql += ",phrase"
    if per != 9:
        sql += ",personality"
    if cloth != 0:
        sql += ",clothes"
    if birth != "xx-xx":
        sql += ",birthday"
    sql += ") VALUES"
    sql += "('" + name + "'," + str(gender) + ","
    if species != 0:
        sql += str(species) + ","
    if phrase != "nah":
        sql += "'"+ phrase + "',"
    if per != 9:
        sql += str(per) + ","
    if cloth != 0:
        sql += str(cloth) + ","
    if birth != "xx-xx":
        sql += "'" + birth + "'"
    if sql[-1] == ",":
        sql = sql[:-1]
    sql += ");"
    print(sql)
    try:
        cursor.execute(sql)
    except:
        print("error!!!")
    cursor.execute("SELECT * FROM cs340_xuna.villagers")
    data = cursor.fetchall()
    # print(data)
    data = villager_converter(data)
    context['data'] = data
    context['villager'] = 0
    return HttpResponseRedirect("/villagers/")
    return render(request,'villager.html',context)

# To make a existed villager to be editing mode

def edit_villager(request, name):
    context = {}
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM cs340_xuna.villagers")
    data = cursor.fetchall()
    data = villager_converter(data)
    print(data)
    for key in data:
        if data[key]['name'] == name:
            data[key]['edit'] = 1
    context['data'] = data
    context['villager'] = 0
    return render(request,'villager.html',context)

# To update info of a existed villager and let it exit from editing mode

def update_villager(request,id, name = "", gender = 0, species = 0,phrase = "" ,per = 9 , cloth = 0, birth = "NULL"):
    print(request)
    context = {}
    cursor = connection.cursor()
    sql = "UPDATE cs340_xuna.villagers SET name = "+ "'" + name + "', gender = " +  str(gender) + ", species = " + str(species) + ", phrase = " + "'" + str(phrase) + "', personality = " + str(per) + ",birthday = '" + birth + "' WHERE id = " + str(id)  + ";"
    print(sql)
    try:
        cursor.execute(sql)
    except:
        print("error!!!")
    cursor.execute("SELECT * FROM cs340_xuna.villagers")
    data = cursor.fetchall()
    # print(data)
    data = villager_converter(data)
    context['data'] = data
    context['villager'] = 0
    return HttpResponseRedirect("/villagers/")
    return render(request,'villager.html',context)

# To delete a existed villager

def delete_villager(request,name):
    context = {}
    cursor = connection.cursor()
    sql = "DELETE FROM cs340_xuna.villagers WHERE name = "+ "'" + name + "';"
    cursor.execute(sql)
    return HttpResponseRedirect("/villagers/")

# To render the material page

def materials(request):
    context = {}
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM cs340_xuna.materials")
    data = cursor.fetchall()
    data = material_converter(data)
    context['data'] = data
    context['material'] = 0
    return render(request,'material.html',context)

# To make an ADD statement for new material and send it to the database

def add_material(request,name,rarity):
    context = {}
    cursor = connection.cursor()
    sql = "INSERT INTO cs340_xuna.materials (name,rarity) VALUES("
    sql += "'"+ name + "','" + str(rarity)+ "');"
    try:
        cursor.execute(sql)
    except:
        print("error!!!")
    return HttpResponseRedirect("/materials/")

# To render the furniture page

def furnitures(request):
    context = {}
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM cs340_xuna.furnitures")
    data = cursor.fetchall()
    print(data)
    data = furniture_converter(data)
    context['data'] = data
    context['furniture'] = 0
    return render(request,'furniture.html',context)

# To make an ADD statement for new furniture and send it to the database

def add_furniture(request,name,source,buy,sell,size,mat1,num1,mat2,num2,mat3,num3,mat4,num4,mat5,num5,mat6,num6):
    # furnitures(request)
    context = {}
    cursor = connection.cursor()
    sql = "INSERT INTO cs340_xuna.furnitures (name,source,bought,sold,size) VALUES("
    sql += "'" + name + "'," + str(source) + "," + str(buy) + "," + str(sell) + "," + str(size) + ");"
    try:
        print(sql)
        cursor.execute(sql)
    except:
        print("error:Add-furniture-furniture")
        return HttpResponseRedirect("/furnitures/")
    mats = [mat1, mat2, mat3, mat4, mat5, mat6]
    nums = [num1, num2, num3, num4, num5, num6]
    sql = "SELECT id FROM cs340_xuna.furnitures WHERE name =  " + "'"  + name + "';"
    cursor.execute(sql)
    fid  = cursor.fetchall()[0][0]
    for i in range(6):
        try:
            if nums[i] != 0:
                sql = "INSERT INTO cs340_xuna.recipe_items (fid,mid,number) VALUES(" + str(fid) + "," + str(mats[i]) + "," + str(nums[i]) + ");"
                # print(sql)
                cursor.execute(sql)
        except:
            print("Error:furniture-add-materials")
            return HttpResponseRedirect("/furnitures/")
    return HttpResponseRedirect("/furnitures/")

# Not finished

def islands(request):
    context = {}
    return render(request,'island.html',context)

def museums(request):
    context = {}
    return render(request,'museum.html',context)

def error(request):
    return render(request,'404.html')
