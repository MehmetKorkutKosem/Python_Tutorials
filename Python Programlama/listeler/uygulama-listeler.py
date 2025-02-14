# 1
markalar=["toyota","Bmw","Renault","mercedes"]
# 2
print(len(markalar))
# 3
x=markalar[0]
y=markalar[3]
a=x+y
print(a)
# 4
sonuc=markalar[2]="togg"
print(sonuc)
# 5
sonuc1="togg"in markalar 
print(sonuc1)
# 6
sonuc=markalar[:3]
print(sonuc)
# 7
sonuc=markalar=markalar+["ford","citroen"]
print(sonuc)
# 8
del markalar[5]
sonuc=markalar
print(sonuc)
# 9
ogrenci1=["yiğit","bilgi","2010",[70,80,90]]
ogrenci2=["ada","bilgi","2011",[70,70,80]]
ogrenci3=["çinar","turan","2017",[60,60,90]]
print(ogrenci1)
print(ogrenci2)
print(ogrenci3)
# 10
ogrenci11=2024-int(ogrenci1[2])
print(ogrenci11)
ogrenci22=2024-int(ogrenci2[2])
print(ogrenci22)
ogrenci33=2024-int(ogrenci3[2])
print(ogrenci33)
#11
top1=0
for i in ogrenci1[3]:
    top1=top1+i
    ort1=top1/len(ogrenci1[3])
    print(ort1)
top2=0
for i in ogrenci2[3]:
        top2=top2+i
        ort2=top2/len(ogrenci2[3])
        print(ort2)
top3=0        
for i in ogrenci3[3]:
      top3 =top3+i
      ort3=top3/len(ogrenci3[3])
      print(ort3)