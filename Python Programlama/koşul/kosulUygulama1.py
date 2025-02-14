# 1. Girilen bir sayının 0-100 arasında olup olmadığını kontrol et.
sayi = int(input("Sayı giriniz: "))
if (sayi > 0) and (sayi <= 100):
    print("Sayı 0 ile 100 arasında.")
else:
    print("Sayı 0 ile 100 arasında değil.")

# 2. Girilen bir sayının pozitif çift sayı olup olmadığını kontrol et.
sayi = int(input("Sayı giriniz: "))
if (sayi > 0) and (sayi % 2 == 0):
    print("Sayı çift pozitif tam sayı.")
else:
    print("Sayı çift pozitif tam sayı değil.")

# 3. Mail adresi ve şifresini alıp doğrula.
mail = input("Adresinizi giriniz: ")
sifre = int(input("Şifrenizi giriniz: "))
if (mail == "samuel@gmail") and (sifre == 345):
    print("Giriş başarılı.")
else:
    print("Giriş başarısız.")

# 4. Girilen 3 sayıyı büyüklük olarak karşılaştır.
sayi0 = int(input("Sayı 1 giriniz: "))
sayi1 = int(input("Sayı 2 giriniz: "))
sayi2 = int(input("Sayı 3 giriniz: "))

if sayi0 > sayi1 and sayi0 > sayi2:
    print(f"{sayi0} en büyük sayı.")
elif sayi1 > sayi0 and sayi1 > sayi2:
    print(f"{sayi1} en büyük sayı.")
else:
    print(f"{sayi2} en büyük sayı.")
# 5. iki vize sıb
vize0=int(input("vize notunuzu giriniz"))
vize1=int(input("vize notunuzu giriniz"))
final=int(input("final notunuzu giriniz"))
ort=((vize0+vize1)/2)*0.6 + final*0.4
if final>=70 :
    print("gecti")
else:    
    
  if final>50 :
    if ort>50:
      print("gecti")
    else:
        print("kaldi")
  else:
    print("kaldi")       
# 6 kişinin boy kilo bilgilerini alıp indeksini hesaplayınız
name=input("isminizi giriniz")
boy=int(input("boyunuzu giriniz"))
kilo=int(input("kilonuzu giriniz"))
index=kilo/(boy**2)
if index>0 and index <=18.4:
  print(f"kilo zayif")
elif index>18.4 and 24.9 :
   print("normal ")
elif index>24.9 and 29.9 :
   print("fazla kilolu")
elif index>24.9 and 34.9 :
   print("obez")
else:
   print("gecersiz")