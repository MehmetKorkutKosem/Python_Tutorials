class person:
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    
    def __repr__(self):#bu şekilde bu özel metodu ezerek kendi özel durumumuzu oluşturabiliriz
        return f"adi {self.name} cinsiyeti{self.gender} yasi {self.age}"
    
    def __del__(self):
        print(f" {self.name} kişisinin verileri silindi ")
m=person("ali",12,"erkek")
print(m)# bu durumu verir <__main__.person object at 0x000002139E605D90>
del m
# meta class
class test():
    pass

sonuc=type(test())
sonuc=type(test)
sonuc=type(2)
sonuc=type(int)#hepsinin temeli type metaclasıdır
print(sonuc)

class base:
    def pr(self):
       return "merhaba"
    
    def add(self):
        self.b=5

# test1=type("title",("temel alddigi siniflar"),"attributeler bu bölüme")
#test1=type("test1",(base,),{})
test1=type("test1",(base,),{"d":5,"add":lambda self: base.add(self)})
a=test1()
sonuc=a.pr()
sonuc=a.d
sonuc=a.b
print(sonuc)