import datetime
# 1 kullanıcıdan isim , yaş ve eğitim bilgilerini alarak ehliyet alabilme durumunu kontrol ediniz
"""name=input("isminizi giriniz: ")
age=int(input("yasinizi giriniz: "))

if age>=18:
    egitim=(input("egitimi bilgilerinizi giriniz: "))
    if egitim=="lise" or egitim=="universite":
       print("basvuru yapmaya uygunsunuz")
    else:
       print("egitim durumunuz uygun olmadigindan dolayi basvuru yapamazsiniz")
else:
   print("yasiniz uygun olmadigindan dolayi basvuramazsiniz")"""

# 2 ogrencinin iki yazılı bir sözlü notunu alıp ortalamayı kakşılaştırın
"""sinav=int(input("birinci sinav notunuzu giriniz"))
sinav1=int(input("ikinci sinav notunuzu giriniz"))
sozlu=int(input("sözlü notunuzu giriniz"))
ort=(sinav+sinav1+sozlu)/3
if ort<=24 :
   sayi=0
   print(f" {ort} ortalamanizin agirlik puani: {sayi}")
elif ort>25 and ort<=44:
   sayi=1
   print(f" {ort} ortalamanizin agirlik puani: {sayi}")
elif ort>44 and ort<=54:
   sayi=2
   print(f" {ort} ortalamanizin agirlik puani: {sayi}")
elif ort>54 and ort<=69:
   sayi=3
   print(f" {ort} ortalamanizin agirlik puani: {sayi}")
elif ort>69 and ort <=84:
   sayi=4
   print(f" {ort} ortalamanizin agirlik puani: {sayi}")
elif ort>84 and ort <=100:
   sayi=5
   print(f" {ort} ortalamanizin agirlik puani:{sayi}") 
else :
   print(f" gecersiz deger girisi") """
# Trafiğe çıkış zamanı alınan bir aracın servis zamanını gün bazlı hesaplayın
usertime=input("deger gir")
usertime=usertime.split('/')
print(usertime[0])
print(usertime[1])
print(usertime[2])
trafigecikis=datetime.datetime(int(usertime[0]),int(usertime[1]),int(usertime[2]))
simdi=datetime.datetime.now()
fark = simdi-trafigecikis
print(fark)

