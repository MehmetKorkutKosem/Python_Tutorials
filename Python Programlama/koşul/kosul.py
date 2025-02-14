kullaniciAdi=input("kullanici adinizi giriniz: ")
sifre=input("lutfen sifrenizi giriniz: ")

if sifre.isalpha():#sifre girisinin tamamını harflerden oluşup oluşmadığını kontrol eder
    print("gecersiz deger girisi", end=" ")#koşulun doğru olması durumunda çıktıyı ekrana verir
else:
  if kullaniciAdi=="samuel" and sifre=="3456":# kullaniciAdi ve sifre girdilerinin herhengi birinin hatalı olması durumunda else durumuna gider ve çıktıyı veriri
    print("giris basarili",end=" ")
  else:
    print("kullanici adi veya sifre yanlis")

kullaniciAdi=input("kullanici adinizi giriniz: ")
sifre=input("lutfen sifrenizi giriniz: ")
if sifre.isalpha():#sifre girisinin tamamını harflerden oluşup oluşmadığını kontrol eder
    print("gecersiz deger girisi", end=" ")#koşulun doğru olması durumunda çıktıyı ekrana verir
else:
  if kullaniciAdi=="samuel" and sifre=="3456":# kullaniciAdi ve sifre girdilerinin herhengi birinin hatalı olması durumunda else durumuna gider ve çıktıyı veriri
    print("giris basarili",end=" ")
  elif kullaniciAdi=="samuel": # ilk koşul durumu hatalı ise ikinci koşul durumuna elif aktarır
    print("kullanici adi dogru")
    print("sifre hatali")
  else:
     print("sifre ve kullanici adi hatali")
