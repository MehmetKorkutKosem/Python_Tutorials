# 1 kullanıcıdan bir dizi al ve bunu ekrana yazdır
sayilar=[]
a=0
a=int(input("gireceğiniz sayi miktarini giriniz"))
while a>0 :
    sayi=int(input("sayi gir"))
    sayilar.append(sayi)
    a-=1
print(sayilar)
y=len(sayilar)
a=y
while y>0 :
    print(sayilar[a-y])
    y-=1
# 2 kullanıcının başlandıç ve bitiş değerlerini belirlediği bir aralık belirle ve arsındaki tek sayıları ekrana yazdır
a=int(input("araligi başlangiç temelini belirleyiniz"))
b=int(input("araligin bitiş degerini belirleyiniz"))
while a<=b :
    if a%2!=0 :
        print(a)

    a+=1    
# 3 sayilari azalan sekilde yazdirma
a=int(input("liste hangi sayiya kadar olsun"))
while a>0 :
    print(a)
    a-=1

# 4 kullanıcidan alacagin sayilari ekrana sirali yazdir
 # 1 . yontem 
numbers=[]
a=int(input("gireceginiz sayi miktarini giriinz"))
sayac=0
while sayac<a :
    sayi=int(input("sayi gir"))
    numbers.append(sayi)
    sayac+=1

numbers.sort()
print(numbers)
# 5 kullanıcıda urün bilgisi alip ekrana yazdir
dict=[]
a=int(input("liste sayisini belirleyiniz"))
sayac=0
while sayac<a :
    name=input("urun ismi")
    price=input("urun fiyati")
    dict.append({"name":name,"price":price})
    sayac+=1
sayac=0
while sayac<a :
    print(dict[sayac])
    sayac+=1