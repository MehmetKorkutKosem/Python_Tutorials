programlama_dilleri=["python","c","java","assembly"]
sonuc=programlama_dilleri[:]#tümünü yazdırır
print(sonuc)

sonuc1=programlama_dilleri[:3] #ikinci indise kadar yazdırır son indis alınmaz
print(sonuc1)
sonuc1=programlama_dilleri[::-1]#tersten yazdırır
print(sonuc1)
sonuc2=programlama_dilleri[-3:-1]
print(sonuc2)
sonuc3=programlama_dilleri[2:]
print(sonuc3)
sonuc4=programlama_dilleri[:-3]
print(sonuc4)
# güncelleme
programlama_dilleri[-1]="php"# son indisi yeni değerle değiştirmiş aluruz
sonuc5=programlama_dilleri
print(sonuc5)
sonuc6=programlama_dilleri+["kotlin","go"]
print(sonuc6)
sonuc7="react"in programlama_dilleri[2]
print(sonuc7)
sonuc8="python"in programlama_dilleri
print(sonuc8)
del programlama_dilleri[2] # ikinci indisteki elemanı siler
sonuc9=programlama_dilleri
print(sonuc9)