# 1-"title" değişkeni içerisindeki karakter sayısı nedir
title="python ile programlama"
değisken=len(title)
print(değisken)
# 2-"title" icerisindeki 'python'kelimesini alın
print(title[:6])
# 3-"title" ilk beş ve son beş karakterini alın
sonuc=title[:6]
sonuc1=title[::-1][:6]
sonuc2=sonuc+sonuc1
print(sonuc2)
# 4-"title" değiskenini tersten yazdır
s1=title[::-1]
print(s1)
# 5-klavyeden girilen öğrencinin bilgilerine göre verilen cümleyi yazdırınız
ad=input("lutfen adinizi giriniz")
soyad=input("lutfen soyadinizi giriniz")
number1=float(input("1.sinav notunuz"))
number2=float(input("2.sinav notunuz"))
total=number1+number2
notort=total/2
print(f"{ad} {soyad} isimli öğrencinin 1. notu{number1},2.notu{number2} ve not ortalamasi{notort}")
