numbers =[1,2,3,4,5]
for x in numbers :# numbe listesi içinden x elemanını alarak çıktıya verir
    print(x) # hello world ekrana beş hello world çıktısı verir
names=["ali","murat","sedat"]
for x in names :
    print(f"ismim {x}")
isim="samet murat"
for x in isim :
    print(x) # strink ifadenin indislerini yazdırır
tuple=(1,2,3,4)
for x in tuple :
    print(x)
tuple=[(1,2),(5,6),(9,5)]# burda ayrı tuple guruplarından oluituğu için yaaılır onların hepsine ulaşmak için başka bir değer daha seçilmesi gerek
for x,y in tuple : #x,b
    print(x)
    print(y)
d={'k1':1,'k2':3,'k3':4}
for key,value in d:
   print(key,value)