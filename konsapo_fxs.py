#冷蔵庫管理の機能を選択する
def refrigerator_choice():
    option=[
        '1.食材を追加',        #食材を新規で追加する
        '2.場所別食材リスト',   #保存場所別に食材をリストアップする
        '3.献立提案',        #冷蔵庫な中身から献立を提案する
        '4.保存場所の追加',    #冷蔵庫内での保存場所を追加する
        '5.終了'#アプリを終了する
    ]
    choice=int(input())
    return choice

#選択された冷蔵庫管理の機能に応じて関数を呼び出す
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

#食材を任意の保存場所に登録する
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

#保存場所別に登録されている食材をリストアップ
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

#登録されている食材から献立を提案する
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

#食材の保存場所を追加する
def append_place():
    select=0
    while select!=2:
        place_input=input('保存場所を追加')
        with open('refrigerator_places.txt',mode='a') as opner:
            opner.write('\n'+place_input)
        print('1.さらに追加する')
        print('2.追加しない')
        select=int(input())
