kursAdi="Btk Akademi Python İle Programlama Dersleri"
website="https://www.btkakademi.gov.tr/"
# 1-'Btk akademi' karakter dizisinin baştaki ve sondaki boşluklarını siliniz.
dny1=kursAdi.strip()
print(dny1)
# 2-'kurs adı değişkenindeki tüm karakterleri küçük harfe çeviriniz.
dny2=kursAdi.lower()
print(dny2)
# 3-website değişkeninde kaç tane '.' karakteri vardır.
dnyx = website.count('.')
print(dnyx)
# 4-website değişkeni https ile mi başlıyor.
dny3=website.startswith("https")
print(dny3)
# 5- tr ile mi bitiyor.
dny4=website.endswith("tr")
print(dny4)
# 6-kursAdi içindeki tüm karakterler harflerden mi oluşuyor.
dny5=kursAdi.isalnum()
# 7-kursAdi değişkenindeki tüm boşluklatı _ ile değitiriniz.
dny6=kursAdi.replace(" ","_")
print(dny6)
# 8-kursAdi değişkenindeki tüm Python kelimesini assembly ile değiştirin.
dny7=kursAdi.replace("Python","assembly")
print(dny7)
# 9-website değişkeni 'www' içeriyor mu?
dny9 = 'www' in website
print(dny9)
# 10-kursAdi değişkenini listeye çeviriniz.
dny8=kursAdi.split()
print(dny8)