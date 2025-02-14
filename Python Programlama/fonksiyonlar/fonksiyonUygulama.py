# kullanıcıdan alınan kelimeyi ve kaç kere yazdırılmasını istediğini alıp fonksiyon kullanarak ekrana yazdıran program
kelime=input("yazdirilmasini istediğiniz kelimeyi giriniz")
dongu=int(input("ne kadar tekrar etmesini istiyorsunuz"))
def tekrar(kelime,dongu):
    for x in range(dongu):# for yerine print(kelime*dongu) şeklinde de yazılabilir ama bu şekilde daha anlaşılır olur
        print(kelime)

tekrar(kelime,dongu)
# kullanıcıdan alınan sayıları bir listeye atan fonksiyon

list=[]
def transformator(*count):
     # list=[]
     for x in count:
         list.append(x)
     return list

print(transformator(1,2,3,4,5,6,7,8,9,10))

# girilen iki sayi arasındaki asal sayıları bulan fonksiyon

a=int(input("sayi giriniz"))                             
b=int(input("sayi giriniz"))
if a>b: 
   temp=a
   a=b
   b=temp
def asalsayi(a,b):
    for x in range(a,b):
        if x==2 :
            print(f"{x} asal sayidir")
        elif x>1 and x%2!=0:
           print(f"{x} asal sayidir")
        else:
            print(f"{x} asal sayi değidir")

asalsayi(a,b)

""" a = int(input("Sayı giriniz: ")) örenği bu şekilde de yazabiliriz
b = int(input("Sayı giriniz: "))
if a > b:
    temp = a
    a = b
    b = temp

def asalsayi(a, b):
    for x in range(a, b):
        if x < 2:
            print(f"{x} asal sayı değildir")
            continue
        for i in range(2, x):
            if x % i == 0:
                print(f"{x} asal sayı değildir")
                break
        else:
            print(f"{x} asal sayıdır")

asalsayi(a, b)""" 

# girilen sayının bölenlerini bulup listeye atan fonksiyon

a=int(input("sayi giriniz"))
list=[]
def bolme(a):
    #list=[]
    for x in range(1,a+1):
       if a%(x)==0:
           list.append(x)
    return list
           

print(bolme(a))