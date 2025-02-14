#girilen iki sayidan hangisi daha büyük
a=int(input("lütfen sayi giriniz"))
b=int(input("lütfen sayi giriniz"))
if(a>b):
    print(f"{a} {b} den daha büyüktür")
else:
    print(f"{b} {a} dan daha büyüktür")   
# kullanicidan iki vize (%60) ve final(%40) notu isteyiy ortalama hesaplayin 
vize=int(input("lutfen notunuzu girirniz"))
vize2=int(input("lutfen notunuzu giriniz"))
final=int(input("lutfen notunuzu giriniz"))
vize*=0.6
vize2*=0.6
vize+=vize2
final*0.4
ort=vize+final
if(ort>=50):
    print(f"{ort} ile geçti")
else:
    print("kaldi")  
# girilen bir sayinin tek mi çift mi olduğu
z=int(input("lutfen sayi giriniz"))     
if(z%2==0) :
    print("cift")
else:
    print("tek")  
# girilen sayinin negatif mi pozitif mmi olduğu durum
v=int(input("sayi gir"))  
if(v>=0):
    print("pozitif")
else:
    print("negatif")    

parola="abc123"
mail="fire@gmail.com"
u=input("lutfen mailini gir")
uc=input("lutfen parolani gir")
if(u==mail and uc==parola):
    print("giris yapildi")
else:
    print("sifre veya parola yanlis")    