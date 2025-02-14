class person:
    pass # boş klas tanımı
class Person:
    deger="invalid"
    def __init__(self,name,age):#init constructor görevi görür
         self.name=name      #self: o anki nesneyi temsil eder self yerine this de kullanılabilir
         self.age=age


p1=Person("ali",33)#p1=Person(name="ali",age=33)
p2=Person("veli",44)#p2=Person(name="veli",age=44)
print(f" name={p1.name} age={p1.age} deger={p1.deger}")
print(f" name={p2.name} age={p2.age} deger={p2.deger}")
p1.deger="valid"
p1.age=55
p1.name="mehmet"
p2.name="ahmet"
p2.age=66
print(f" name={p1.name} age={p1.age} deger={p1.deger}")
print(f" name={p2.name} age={p2.age} deger={p2.deger}")