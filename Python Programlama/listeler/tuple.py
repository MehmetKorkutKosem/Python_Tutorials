#tuple elemanları değiştirirlemez
tuple=(1,"iki",3)
list=[1,2,3]
list[0]=5#listenin sıfırıncı indeksindeki elaman değişir
tuple(0)=5#tuple bu durumda hata verir çünkü yapısı gereği elemanları değiştirilemez
print(list)
print(tuple)
letter=("a","c")+tuple#tuple başka bir tuple ile birleştirilebilir
print(letter)
