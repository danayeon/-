'''
from flask import Flask
app=flask(__name__)

@app.route("/")
'''
def select(comment,list):
    print(comment)
    i=0
    for item in list:
        print(str(i)+item)
        i+=1
    print(str(i)+'検索')
    num=int(input())
    if num==i:
        word=input('検索したい言葉を入力')
        for item in list:
            if word==item:
                print(word+'だね！')
                return word
                break
            else:
                print('他の言葉で探してみてね')
                select(comment,list)
    else:
        return list[num]

#今の気分の選択
#今の気分の選択肢を表示する 縦にいくつかリスト表示 検索機能？
feels=['こってり','あっさり','がっつり','さっぱり']
feel=select('今の気分は?',feels)

#メインとなる食材の選択
#肉 麺 魚 野菜
stuffs=['肉類','麺類','魚類','野菜類','米']
stuff=select('メインの食材は何がいい？',stuffs)
if stuff=='肉類':
    meets=['牛肉','豚肉','鶏肉','その他の肉']
    stuff=select('どんなお肉がいい？',meets)
elif stuff=='魚類':
    fish=['青魚','白身魚','赤身']
    stuff=select('どんな魚がいい？',fish)
elif stuff=='野菜類':
    vegetables=['大根','人参','キャベツ','白菜','その他の野菜']
    stuff=select('どんな野菜がいい?',vegetables)
elif stuff=='麺類':
    noodles=['うどん','ラーメン','そば','その他の麺']
    stuff=select('どんな麺がいい？',noodles)

#今食べたい食べ物の種類を選択させる
#和食 中華 フレンチ イタリアンなど
regions=['和食','中華','イタリアン','フレンチ','韓国','スパニッシュ','洋食']
region=select('どの種類の料理が食べたい？',regions)

print(feel+'で'+stuff+'がメインの'+region+'だね！')


menu_1={'name':'ハンバーグ','feel':'がっつり','stuff':'肉類','region':'洋食'}
menu_2={'name':'そうめん','feel':'あっさり','stuff':'麺類','region':'和食'}
menu_3={'name':'エビチリ','feel':'こってり','stuff':'魚類','region':'中華'}
menu_4={'name':'お茶漬け','feel':'さっぱり','stuff':'米','region':'和食'}


menus=[menu_1,menu_2,menu_3,menu_4]
menus_rank={}
for menu in menus:
    match=0
    if menu['feel']==feel:
        match+=1
    if menu['stuff']==stuff:
        match+=1
    if menu['region']==region:
        match+=1
    menus_rank[menu['name']]=match
print('おすすめの料理は'+max(menus_rank,key=menus_rank.get)+'だよ！')
