
#Flaskなどの必要なライブラリをインポートする
from flask import Flask,render_template,request,redirect,url_for
import numpy as np
import sys
sys.path.append('/Users/nishitatoraki/anaconda3/lib/python3.7/site-packages')
import requests
from urllib.request import urlopen
import random


#txtデータによるDBにアクセスするキーワードを登録する
places_db='refrigerator_places.txt'
foods_db='refrigerator_foods.txt'
menu_db='konsapo_dish_menu.txt'

#自身の名称をappという名前でインスタンス化する
app=Flask(__name__)

#ウェブアプリケーション用のルーティングを記述
#メインメニューにアクセスしたとき
@app.route('/')
def refrigerator_mainmenu():
    title='メインメニュー-食材管理'
    char_word='機能を選択してね！'
    return render_template('konsapo_refrigerator_mainmenu.html',char_word=char_word,title=title)

#「食材を追加」にアクセスしたとき
@app.route('/reg_data',methods=['GET','POST'])
def reg_data():
    title='食材を追加-食材管理'
    with open(places_db) as f:
        places=[s.strip() for s in f.readlines()]
    if len(places)==0:
        char_word='保存場所がないよ！'
        return render_template('konsapo_refrigerator_foodreg.html',char_word=char_word,error_message=error_message,title=title)
    else:
        char_word='追加する食材の情報を入力してね！'
        food_place=''
        for place in places:
            food_place+='<option value="'+place+'" name="place" for="place">'+place+'</option>'
        return render_template('konsapo_refrigerator_foodreg.html',char_word=char_word,food_place=food_place,title=title)
#食材の情報の入力が完了して、登録ボタンが押されたとき
@app.route('/reg_data/fin',methods=['GET','POST'])
def reg_data_2():
    title='食材を追加-食材管理'
    if request.method=='POST':
        food=request.form['food_name']
        amount=request.form['food_amount']
        limit=request.form['food_limit']
        place=request.form['food_place']
        with open(foods_db,mode='a') as f:
            f.write(food+','+amount+','+limit+','+place+'\n')
        char_word=food+'(賞味期限:'+limit+')を'+amount+'つ'+place+'に追加したよ！'
        return render_template('konsapo_refrigerator_foodreg_fin.html',char_word=char_word,title=title)

#「場所別食材リスト」にアクセスしたとき
@app.route('/foodlist',methods=['GET','POST'])
def foodlist():
    title='食材リスト-食材管理'
    with open(places_db) as f:
        places=[s.strip() for s in f.readlines()]
    if len(places)==0:
        char_word='保存場所がないよTT'
        return render_template('konsapo_refrigerator_foodslist.html',char_word=char_word,title=title)
    else:
        food_place=''
        char_word='確認したい場所を選択してね！'
        for place in places:
            n=0
            food_place+='<tr><td><div class="checkbox"><input id="input'+str(n)+'" type="checkbox" name="place" value="'+place+'" for="'+place+'"><label for="input'+str(n)+'">'+str(n)+place+'</label ></div></td></tr>'
            n+=1
        return render_template('konsapo_refrigerator_foodslist.html',char_word=char_word,food_place=food_place,title=title)
#確認する保存場所が選択されたとき   要改善
@app.route('/foodlist/result',methods=['GET','POST'])
def foodlist_result():
    title='食材リスト-食材管理'
    char_word='食材のリストだよ！'
    food_list=''
    if request.method=='POST':
        with open(places_db) as f:
            places=[s.strip() for s in f.readlines()]
        with open(foods_db) as f:
            foods=[s.strip() for s in f.readlines()]
        for place in places:
            try:
                place_name=request.form['place']
                for food in foods:
                    food_data=food.rstrip().split(',')
                    if food_data[3]==place_name:
                        food_list+='<tr><th>'+food_data[0]+'</th><td>'+food_data[2]+'</td><td>'+food_data[1]+'</td><td>'+food_data[3]+'</td></tr>'
            except:
                place_name='null'
                food_list='null'
        return render_template('konsapo_refrigerator_foodslist_result.html',char_word=char_word,place=place_name,food_list=food_list,title=title)

#「献立提案」にアクセスしたとき
@app.route('/suggest_menu',methods=['GET','POST'])
def suggest_menu():
    title='献立提案-食材管理'
    char_word='オススメの料理は・・・'
    suggestion={}
    menus=[]
    suggested_menu=''
    sg='クックパッド'
    with open(foods_db) as f:
        foods=[s.strip() for s in f.readlines()]
    food_names=[]
    for food in foods:
        food_data=food.rstrip().split(',')
        food_name=food_data[0]
        food_names.append(food_name)

    for j in food_names:
        sg+=' '
        sg+=j
    url='https://www.google.co.jp/search'
    req=requests.get(url,params={'q':sg})
    url=req.url
    suggested_menu='<a href='+url+'>'+url+'</a><br>'
    last_message='クリックでレシピを表示できるよ！'


#    with open(menu_db) as f:
#        menu_data=[s.strip() for s in f.readlines()]
#    for item in menu_data:
#        item_data=item.rstrip().split(',')
#        menus.append(item_data)
#    for menu in menus:
#        i=0
#        for stuff in menu:
#            if stuff in food_names:
#                i+=1
#        suggestion[menu[0]]=i
#    num=max(suggestion.values())
#    for k,v in suggestion.items():
#        if num==v:
#            try:
#                url='https://www.google.co.jp/search'
#                req=requests.get(url,params={'q':k+'クックパッド'})
#                url=req.url
#                suggested_menu='<a href='+url+'>'+k+'</a><br>'
#                last_message='クリックでレシピを表示できるよ！'
#            except:
#                suggested_menu=k
#                last_message='URLを取得できないよTT  インターネット環境を確認してね！'

    return render_template('konsapo_refrigerator_suggestmenu.html',char_word=char_word,suggested_menu=suggested_menu,last_message=last_message,title=title)

#「保存場所の追加」にアクセスしたとき
@app.route('/append_place',methods=['GET','POST'])
def append_place():
    title='保存場所の追加-食材管理'
    char_word='追加する保存場所を入力してね！'
    return render_template('konsapo_refrigerator_appendplace.html',char_word=char_word,title=title)
#保存場所の入力が完了して登録ボタンが押されたとき      未完
@app.route('/append_place/fin',methods=['GET','POST'])
def append_place_2():
    title='保存場所の追加-食材管理'
    if request.method=='POST':
        place=request.form['place']
        with open(places_db,mode='a') as f:
            f.write(place+'\n')
        char_word='新しい保存場所　'+place+'　を登録したよ！'
    return render_template('konsapo_refrigerator_appendplace_fin.html',char_word=char_word,title=title)
#ガチャ
@app.route('/gacha',methods=['GET','POST'])
def gacha():
    title='ガチャ-食材管理'
    return render_template('konsapo_refrigerator_gacha.html',title=title)
#ガチャリザルト
@app.route('/gacha/result',methods=['GET','POST'])
def gacha_result():
    title='ガチャ結果-食材管理'
    charas=[['きつね','https://stockmaterial.net/wp/wp-content/uploads/img/animal_fox01_01.png',1],['うさぎ','https://www.sozailab.jp/db_img/sozai/128/61d1df199eb81816f99b982391e759fb.jpg',2],['リス','https://stockmaterial.net/wp/wp-content/uploads/img/animal_squirrel01_01.png',3]]
    num=random.randint(1,8)
    if num<=3:
        num=1
    elif num==4:
        num=2
    elif num>=5:
        num=3
    for chara in charas:
        if chara[2]==num:
            animalimg='<img src="'+chara[1]+'"alt="'+chara[0]+'">'
            animalname=chara[0]
    return render_template('konsapo_refrigerator_gacharesult.html',animalname=animalname,animalimg=animalimg,title=title)


if __name__=='__main__':
    app.run(debug=True)
