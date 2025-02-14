mesaj="btk akademi,python,python kursu"
sonuc=mesaj.upper()#karakterleri büyütür
print(sonuc)
sonuc=mesaj.lower()#upper metodunun tam tersini yapar
print(sonuc)
sonuc=mesaj.title()#karakter kümelerinin başlangıçlarındaki karakterleri büyütür
print(sonuc)
sonuc="abc".islower()#tüm karakterlerin küçük olup olmadığını sorgular
print(sonuc)
sonuc=mesaj.strip() #baştaki ve sondaki indisteki karakteri siler
print(sonuc)
sonuc=mesaj.split(",")#listeye dönüştürür
print(sonuc)
sonuc=mesaj.startswith("a")# a karakteri ile başlayıp başlamadığını kontrol eder
print(sonuc)
sonuc=mesaj.endswith("s")# s karakteri ile sonlanıp sonlanmadığını kontrol eder
print(sonuc)
sonuc=mesaj.replace("python","javascript")# yer değiştirme
print(sonuc)
