#データベース
'''
import pymysql.cursors

conn=pymysql.connect(host=)
'''
places_db='refrigerator_places.txt'
foods_db='refrigerator_foods.txt'
menu_db='konsapo_dish_menu.txt'

#requestsのインポート
import sys
sys.path.append('/Users/nishitatoraki/anaconda3/lib/python3.7/site-packages')
import requests
from urllib.request import urlopen
#冷蔵庫の中身を記録する
menu_1=['親子丼','鶏肉','卵','玉ねぎ','ネギ']#親子丼
menu_2=['カレー','玉ねぎ','人参','じゃがいも','牛肉']#カレー
menu_3=['オムライス','卵','米','にんにく','ケチャップ']#オムライス
menu_4=['ロールキャベツ','キャベツ','トマト','コンソメ','豚肉']#ロールキャベツ
menu_5=['ハンバーグ','卵','パン粉','牛肉','ケチャップ']
#menus=[menu_1,menu_2,menu_3,menu_4,menu_5]
places=[]
foods=[]
#メニュー
def choice_1(choice):
    if choice==1:
        reg_data()
    elif choice==2:
        listup()
    elif choice==3:
        suggest()
    elif choice==4:
        append_place()
    elif choice==5:
        choice=5
    else:
        print('正しい番号を選択してください')


#食材を追加
#全部手入力
#レシートから読み込んで賞味期限だけ手入力
#画像で物を理解して賞味期限だけ手入力
#全部画像で理解する
def reg_data():
    with open(places_db) as f:
        places=[s.strip() for s in f.readlines()]
    if len(places)==0:
        print('保存場所がありません')
    else:
        food=input('食材名を入力')
        count=input('数量を入力')
        date=input('賞味期限を入力')
        print('収納場所を選択')
        i=0
        for place in places:
            print(str(i)+place)
            i+=1
        place=places[int(input())]
        with open(foods_db,mode='a') as f:
            f.write(food+','+count+','+date+','+place)
        #foods.append([food,count,date,place])

#保存場所別に食材をリストアップする
def listup():
    i=0
    with open(places_db) as f:
        places=[s.strip() for s in f.readlines()]
    for place in places:
        print(str(i)+place)
        i+=1
    place=int(input('確認したい場所を選択'))
    place_selected=places[place]
    with open(foods_db) as f:
        foods=[s.strip() for s in f.readlines()]
    for food in foods:
        food_data=food.rstrip().split(',')
        if food_data[3]==place_selected:
            print(food_data[0]+' 数量:'+food_data[1]+' 賞味期限:'+food_data[2])

#冷蔵庫な中身から献立を提案する
def suggest():
    suggestion={}
    menus=[]
    with open(foods_db) as f:
        foods=[s.strip() for s in f.readlines()]
    food_names=[]
    for food in foods:
        food_data=food.rstrip().split(',')
        food_name=food_data[0]
        food_names.append(food_name)
    with open(menu_db) as f:
        menu_data=[s.strip() for s in f.readlines()]
        #print(menu_data)
    for item in menu_data:
        item_data=item.rstrip().split(',')
        menus.append(item_data)


    for menu in menus:
        i=0
        for stuff in menu:
            if stuff in food_names:
                i+=1
        suggestion[menu[0]]=i
    num=max(suggestion.values())
    for k,v in suggestion.items():
        if num==v:
            print('オススメの料理は'+k+'です')
            url='https://www.google.co.jp/search'
            req=requests.get(url,params={'q':k+'クックパッド'})
            print(req.url)
    #print('この機能はまだ利用できません')

#冷蔵庫内での保存場所を追加する
def append_place():
    select=0
    while select!=2:
        #print('収納場所を追加')
        place_input=input('収納場所を追加')
        with open('refrigerator_places.txt',mode='a') as opner:
            opner.write('\n'+place_input)
        #places.append(input())
        print('1.さらに追加する')
        print('2.追加しない')
        select=int(input())


choice=0
while choice!=5:
    print('1.食材を追加')        #食材を新規で追加する
    print('2.場所別食材リスト')   #保存場所別に食材をリストアップする
    print('3.献立提案')         #冷蔵庫な中身から献立を提案する
    print('4.保存場所の追加')     #冷蔵庫内での保存場所を追加する
    print('5.終了')             #アプリを終了する
    choice=int(input())
    choice_1(choice)

    #print(str(choice)+str(places)+str(foods))
'''
    print('1.食材を追加')
    print('2.終了')
    choice=int(input())
    if choice==1:
        reg()
    else:
        for food in foods:
            print(food)
'''
