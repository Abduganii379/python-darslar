name=['ali',"abdulloh",'abdugani','hali','jorilloh']
for n in name:
    print(f'Assalomu aleykom {n}')
nombers=list(range(10,100))
for nomber in nombers:
    print(f"{nomber**3}")
print('5 ta sevimliy kinolarni kiriting')
kinolar=[]
for k in range(5):
    kinolar.append(input(f'{k+1}- kinoni ismini kiriting>>>>'))
print(kinolar)    
person=int(input(f"bugun neshda odam bilan korishdiz?>>"))
ism=[]
for i in range(person):
    ism.append(input(f'{i+1}- odam ismini kiriting>>>>'))
print(ism)    
cars=["toyota","mazda",'hundai','gm','kia']
for car in cars:
    if car!='gm':
        print(car.title())
    else:
        print(car.upper())
ism=input('login ism kiriting>>>')
if ism=="admin":
    print('''hush kelipsiz admin,
foydalanuzilar royhatini korasmi?''')
else:
    print("hush kelipsiz")
print("ikkta son kiriting")
x=int(input("1-soni kiriting"))
y=int(input("2-soni kiriting"))
if x==y:
    print("sonlar teng")
son=int(input('son kiriting>>>'))
if son>=0:
    print("musbat son")
else:
    print("manfiy son")
sonlar=int(input('son kiriting>>>'))
if sonlar%2:
   print("juvt son kiriting>")
else:
   print("rahmat")
yosh=int(input('yoshingizni kiriting>>'))
if yosh<=4 or yosh>=60:
   narh="bepul"
elif yosh<=18 :
   narh=10000
elif yosh>=18 :
   narh=20000 
print(f'sizga kirish {narh}')
goods=["olma","shakar","un","kalbasa","kola","fanta","limon",'sir','uksus',"non"]
savat=[]
for s in range(5):
    savat.append(input(f"{s+1}- mahsulotni kiriting>>>"))
bor_mahsulot=[]
yoq_mahsulot=[]    
for good in savat:    
    if good in goods:
       bor_mahsulot.append(good) 
   
    else:
        yoq_mahsulot.append(good)
if bor_mahsulot:
       print(f"do'konda {savat} bor")
elif yoq_mahsulot:
       print(f"do'konda {savat} yo'q")
foydalanuvchilar=['ali','vali','admin','abdugani','doni']
login=input('yangi login kiriting>>>')
if login in  foydalanuvchilar:
    print('login bant')
else :
    print("rahmat")  
       
    
 
        
    
          
          